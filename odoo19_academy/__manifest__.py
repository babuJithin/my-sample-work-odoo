{
    "name": "Academy Sequence Demo (Odoo 19)",
    "version": "19.0.1.0.0",
    "category": "Tools",
    "summary": "Educational demo: custom sequence in create()",
    "license": "LGPL-3",
    "author": "Infintor",
    "website": "https://www.infintor.com",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence.xml",
        "views/course_enrollment_views.xml"
    ],
    "installable": True,
    "application": True
}