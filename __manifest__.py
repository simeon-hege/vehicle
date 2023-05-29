# -*- coding: utf-8 -*-
{
    'name': "vehicle",

    'summary': "For the purpose of traking vehicle milage.",

    'description': "This module is specifically designed to track vehicle milage and link it to vehicle and delivery or sale orders",

    'author': "Simeon Hege",
    #'website': "http://erp.cedarcreekfurniture.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/vehicle.xml',
        'views/milage_entry_line_view.xml',
        'views/sale_order_view.xml',
        'views/stock_move_view.xml', 
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
