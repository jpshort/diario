# -*- coding: utf-8 -*-
{
    'name': "Asignar Diario",

    'summary': """Asingacion de Diario """,

    'description': """
        Asignacion de Diario
    """,

    'author': "Pedro Nunez Araujo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],
    'data'   : ['views/views.xml']
}
