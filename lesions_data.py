from flask_babel import lazy_gettext as _

lesions = [
    {
        "name": _("Lentigo Maligna Melanoma"),
        "short_description": _("Appears in older adults, spreads to lymph nodes."),
        "long_description": _("Occurs mainly in older people, especially women. It begins as a flat brown or brown-black spot. It has a slow, many-year course and a relatively good prognosis. This type of melanoma most often appears on the face. It causes metastases to nearby lymph nodes."),
        "image": "lentigo1.jpg",
        "images": ["lentigo1.jpg", "lentigo2.jpg", "lentigo3.jpg", "lentigo4.jpg", "lentigo5.jpg"] 
    },
    {
        "name": _("Superficial Spreading Melanoma"),
        "short_description": _("Most common type, spreads along the surface before going deeper."),
        "long_description": _("Usually develops on the basis of a mole. Most often affects middle-aged individuals, although it can also occur in children. It usually begins with a slow superficial growth phase, then the tumor grows vertically, infiltrating the skin and subcutaneous tissue. At that point, it begins to metastasize. It often appears on the trunk (more often in men) or on the legs and mucous membranes (more often in women)."),
        "image": "superficial1.jpg",
        "images": ["superficial1.jpg", "superficial2.jpg", "superficial3.jpg", "superficial4.jpg", "superficial5.jpg"]
    },
    {
        "name": _("Nodular Melanoma"),
        "short_description": _("Aggressive, fast-growing nodule, metastasizes quickly."),
        "long_description": _("Arises on the basis of a pigmented mole or on healthy skin. This type of melanoma progresses quickly and has a poor prognosis. Men are more frequently affected than women. The lesion most commonly appears on the head, neck, or trunk. It can be a colorless, brown, red, or black nodule, which grows vertically from the start and rapidly causes metastases."),
        "image": "nodular1.jpg",
        "images": ["nodular1.jpg", "nodular2.jpg", "nodular3.jpg", "nodular4.jpg", "nodular5.jpg"]
    },
    {
        "name": _("Acrolenitiginous Melanoma"),
        "short_description": _("Rare type, appears on palms, soles, or under nails."),
        "long_description": _("A melanoma with relatively slow growth, occurring mainly in middle-aged individuals. It affects the hands, soles of the feet, or the nail matrix. These are enlarging flat brown or black patches that cause metastases to lymph nodes."),
        "image": "acral1.jpg",
        "images": ["acral1.jpg", "acral2.jpg", "acral3.jpg", "acral4.jpg", "acral5.jpg"]
    },
    {
        "name": _("Amelanotic Melanoma"),
        "short_description": _("Rare, skin-colored or pink lesion, often diagnosed late."),
        "long_description": _("This type of melanoma is very rare. The lesion arises on previously unchanged skin and has the color of normal skin or is pinkish. Because of this, it is often diagnosed very late, which further worsens the already poor prognosis."),
        "image": "amelanotic1.jpg",
        "images": ["amelanotic1.jpg", "amelanotic2.jpg", "amelanotic3.jpg", "amelanotic4.jpg", "amelanotic5.jpg"]
    },
    {
        "name": _("Oral mucosal melanoma"),
        "short_description": _("Dark, painless spot or nodule in the mouth, metastasizes early."),
        "long_description": _("In about 5 percent of cases, melanoma is located on the mucous membranes of the oral cavity. It is most often a dark spot or a soft, dark, well-vascularized nodule. Such a nodule is usually painless. The prognosis is poor, as the tumor grows vertically from the beginning and quickly metastasizes. Therefore, any dark lesion on the oral mucous membranes without a clear cause should raise suspicion of melanoma."),
        "image": "No_image_available.png",
        "images": ["No_image_available.png"]
    },
    {
        "name": _("Vulvovaginal melanoma"),
        "short_description": _("Rare, aggressive lesion on labia or lower vagina."),
        "long_description": _("Melanomas in this location are rare. They mainly affect the labia minora and the lower third of the vagina. Most commonly, women over 50 are affected. Melanoma in this location usually develops from a pigmented mole. It is a spot or nodule with a tendency to bleed and associated itching. It grows and metastasizes quickly."),
        "image": "No_image_available.png",
        "images": ["No_image_available.png"]
    }

]
