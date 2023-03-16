# -*- coding: utf-8 -*-
{
    'name': "Amazon SP-API",
    'description': """Amazon SP-API""",
    'author': "RoboLabs",
    'website': "http://www.robolabs.lt",
    'license': 'Other proprietary',
    'version': '1.0',
    'depends': ['robo', 'nurasymo_aktas'],
    'data': [
        'security/res_groups.xml',
        'data/product_category_data.xml',
        'data/product_template_data.xml',
        'data/ir_cron_data.xml',
        'data/ir_config_parameter_data.xml',
        'data/amazon_sp_configuration_data.xml',
        'data/amazon_sp_region_data.xml',
        'data/amazon_sp_marketplace_data.xml',
        'data/amazon_sp_product_data.xml',
        'security/ir.model.access.csv',
        'views/menu_items.xml',
        'views/amazon_sp_configuration_views.xml',
        'views/amazon_sp_region_views.xml',
        'views/amazon_sp_marketplace_views.xml',
        'views/amazon_sp_order_views.xml',
        'views/amazon_sp_order_line_views.xml',
        'views/amazon_sp_inventory_act_views.xml',
        'views/amazon_sp_inventory_act_line_views.xml',
        'views/amazon_sp_inventory_act_type_views.xml',
        'views/amazon_sp_product_views.xml',
        'views/amazon_sp_product_category_views.xml',
        'views/amazon_sp_order_report_views.xml',
        'views/amazon_sp_tax_rule_views.xml',
        'views/amazon_sp_order_import_job_views.xml',
        'wizard/robo_company_settings_views.xml',
        'wizard/amazon_sp_order_import_wizard_views.xml',
    ],
    'installable': True,
}
