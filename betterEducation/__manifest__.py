{
    "name": "betterEducation",
    "version": "14.0.1.0.0",
    "summary": "Gestiona los datos de tu escuela en solo lugar",
    "description": "beta",
    "author": "Renzo Valentin",
    "website": "https://github.com/renzofbn/betterEducation",
    "sequence": -100,
    "depends": [
        "mail",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/school_student.xml",
        "views/school_teacher.xml",
        "views/school_subject.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
