from flask_babel import lazy_gettext as _

lesions = [
    {
        "name": _("Benign Nevus"),
        "short_description": _("Common benign mole, usually brown and symmetrical."),
        "long_description": _("Melanocytic nevi, or moles, are usually uniform in color, with regular borders and symmetry. While mostly harmless, any changes in size, shape, or color should be monitored."),
        "image": "nevus1.jpg",
        "images": ["nevus1.jpg", "nevus2.jpg", "nevus3.jpg"]
    },
    {
        "name": _("Seborrheic Keratosis"),
        "short_description": _("Warty, stuck-on appearance; non-cancerous."),
        "long_description": _("These lesions often appear waxy or wart-like, and may look alarming but are benign. Commonly seen in older adults and can vary in color from light tan to black."),
        "image": "keratosis1.jpg",
        "images": ["keratosis1.jpg", "keratosis2.jpg"]
    },
    {
        "name": _("Superficial Spreading Melanoma"),
        "short_description": _("Most common type, spreads along the surface before going deeper."),
        "long_description": _("Superficial spreading melanoma starts by growing along the top layer of the skin. Over time, it may begin to grow vertically into deeper layers. It often appears as a flat or slightly raised patch with irregular borders and varying colors."),
        "image": "superficial1.jpeg",
        "images": ["superficial1.jpeg", "superficial2.jpeg"]
    },
    {
        "name": _("Nodular Melanoma"),
        "short_description": _("Aggressive, fast-growing melanoma that forms a bump or node."),
        "long_description": _("Nodular melanoma often appears as a dark bump that is firm to the touch and grows rapidly. Unlike superficial spreading melanoma, it tends to grow vertically much earlier, making early detection crucial."),
        "image": "nodular1.jpeg",
        "images": ["nodular1.jpeg", "nodular2.jpeg"]
    },
    {
        "name": _("Lentigo Maligna Melanoma"),
        "short_description": _("Appears on sun-damaged skin, usually in older adults."),
        "long_description": _("Lentigo maligna melanoma typically forms on the face, scalp, or neck of older adults with significant sun exposure history. It begins as a flat, tan or brown patch (lentigo maligna) and may slowly darken or become raised over time."),
        "image": "lentigo1.jpg",
        "images": ["lentigo1.jpg", "lentigo2.jpg"]
    },
    {
        "name": _("Acral Lentiginous Melanoma"),
        "short_description": _("Rare type, appears on palms, soles, or under nails."),
        "long_description": _("Acral lentiginous melanoma is more common in people with darker skin tones and often shows up on the hands, feet, or beneath fingernails and toenails. It may look like a dark stripe or spot and is frequently misdiagnosed due to its unusual location."),
        "image": "acral1.jpg",
        "images": ["acral1.jpg", "acral2.jpg"]
    }
]
