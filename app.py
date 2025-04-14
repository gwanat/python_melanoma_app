from flask import Flask, render_template, request, session, redirect, g
from flask_babel import Babel, _,lazy_gettext as _l, gettext
from lesions_data import lesions

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
babel = Babel(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

def get_locale():
    if 'lang' in request.args:
        lang = request.args.get('lang')
        if lang in ['en', 'pl']:
            session['lang'] = lang
            return session['lang']
    elif 'lang' in session:
        return session.get('lang')
    return request.accept_languages.best_match(['en', 'pl'])

def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone

babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)

@app.route('/setlang')
def setlang():
    lang = request.args.get('lang', 'en')
    session['lang'] = lang
    return redirect(request.referrer)

@app.context_processor
def inject_babel():
    return dict(_=gettext)

@app.context_processor
def inject_locale():
    return {'get_locale': get_locale}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/abcd_formula")
def abcd_formula():
    return render_template("abcd_formula.html")

@app.route("/diagnostics", methods=["GET", "POST"])
def diagnostics():
    if request.method == "POST":

        asymmetry = int(request.form["asymmetry"])
        border = int(request.form["border"])
        colors = request.form.getlist("colors")
        structures = request.form.getlist("structures")
        
        color_count = len(colors)
        structure_count = len(structures)
        tds = (1.3 * asymmetry) + (0.1 * border) + (0.5 * color_count) + (0.5 * structure_count)

        
        if tds <= 4.75:
            tds_message = _("Based on the TDS, the lesion is likely benign.")
        elif 4.75 < tds <= 5.45:
            tds_message = _("Based on the TDS, the lesion is suspicious.")
        else:
            tds_message = _("Based on the TDS, the lesion is likely malignant.")


        color_weights = {
            "C_White": 0.5,
            "C_Blue": 0.8,
            "C_DarkBrown": 0.5,
            "C_LightBrown": 0.6,
            "C_Black": 0.5,
            "C_Red": 0.5
        }

        structure_weights = {
            "Pigment_Networks": 0.5,
            "Pigment_Dots": 0.5,
            "Pigment_Globules": 0.6,
            "Branched_Streaks": 0.6,
            "Structureless_Areas": 0.6
        }
        
        new_tds = (0.8 * asymmetry) + (0.1 * border)
        for color in colors:
            new_tds += color_weights.get(color, 0)
        for structure in structures:
            new_tds += structure_weights.get(structure, 0)


        if new_tds <= 4.85:
            new_tds_message = _("Based on the improved TDS, the lesion is likely benign.")
        elif 4.85 < new_tds < 5.45:
            new_tds_message = _("Based on the improved TDS, the lesion is suspicious.")
        else:
            new_tds_message = _("Based on the improved TDS, the lesion is likely malignant.")

        return render_template(
            "diagnostics.html",
            tds=round(tds, 2),
            tds_message=tds_message,
            new_tds=round(new_tds, 2),
            new_tds_message=new_tds_message
        )

    return render_template("diagnostics.html")

@app.route("/characteristics")
def characteristics():
    return render_template("characteristics.html", lesions=lesions)

@app.route("/publications")
def publications():
    return render_template("publications.html")

@app.route("/industry")
def industry():
    return render_template("industry.html")

if __name__ == "__main__":
    app.run(debug=True)