# Copyright (C) 2025 - ATSTi
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Odoo - Chatwoot / HelpDesk',
    'version': '18.0',
    'category': 'Others',
    'license': 'AGPL-3',
    'sequence': 2,
    'summary': 'Chamados do Chatwoot no Helpdesk',
    'description': """
Integração Odoo com Chatwoot
Este módulo adiciona campos e funcionalidades relacionadas a dados de conversas 
associadas ao helpdesk, permitindo registro de conversas do Chatwoot como tickets no Odoo.
    """,
    'author': 'ATSTi Soluções',
    'maintainer': 'Mauricio-ATS, ATSTi',
    'website': 'https://github.com/ATSTI/ats-odoo',
    'depends': [
        'helpdesk_mgmt',
        'chatwoot_odoo'
    ],
    'data': [
        'views/helpdesk_view.xml',
    ],
    'installable': True,
    'application': False,
}
