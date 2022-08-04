# -*- coding: utf-8 -*-
{
    'name': 'betterEducation',
    'version': '0.9',
    'summary': 'Gestiona los datos de tu escuela en solo lugar',
    'description': "beta",
    'author': "Renzo Valentin",
    'website': "https://github.com/renzofbn/education",
    'sequence': -100,
    'depends': [
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/menu.xml',
        'views/main_menu.xml',
        'views/school_student.xml',
        'views/school_teacher.xml',
        'views/school_subject.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

