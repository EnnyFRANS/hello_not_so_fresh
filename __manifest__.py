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
    'depends': ['base'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
