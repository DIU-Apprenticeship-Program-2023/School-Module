# -*- coding: utf-8 -*-
{
    'name': "School Module",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Sakib",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        # security
        'security/ir.model.access.csv',

        # All Views
        'views/student.xml',
        'views/teacher.xml',
        'views/course.xml',
        'views/section.xml',
        'views/registration.xml',

        # MenuItems
        'views/menus.xml',
    ],
    "installation": True,
    "auto_install": True,
    "auto_installation": True,
}
