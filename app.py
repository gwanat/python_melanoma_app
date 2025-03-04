from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

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
            tds_message = "Based on the TDS, the lesion is likely benign."
        elif 4.75 < tds <= 5.45:
            tds_message = "Based on the TDS, the lesion is suspicious."
        else:
            tds_message = "Based on the TDS, the lesion is likely malignant."


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
            new_tds_message = "Based on the improved TDS, the lesion is likely benign."
        elif 4.85 < new_tds < 5.45:
            new_tds_message = "Based on the improved TDS, the lesion is suspicious."
        else:
            new_tds_message = "Based on the improved TDS, the lesion is likely malignant."

        return render_template(
            "diagnostics.html",
            tds=round(tds, 2),
            tds_message=tds_message,
            new_tds=round(new_tds, 2),
            new_tds_message=new_tds_message
        )

    return render_template("diagnostics.html")

if __name__ == "__main__":
    app.run(debug=True)