{
    'name': 'Hello Not So Fresh',
    'version': '1.0',
    'summary': 'Un module Odoo de base réutilisable',
    'description': """
        Ce module de base Odoo peut être utilisé comme point de départ
        pour créer de nouveaux modules personnalisés.
    """,
    'author': 'Ton Nom ou Entreprise',
    'maintainer': 'Ton Nom ou Entreprise',
    'website': 'https://tonsite.com',
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/res_partner_data.xml',
        'views/res_partner_views.xml',
        'views/hello_fresh_views.xml',
        'views/hello_fresh_recipe_views.xml',
        'report/recipe_reports.xml',
        'report/recipe_templates.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
