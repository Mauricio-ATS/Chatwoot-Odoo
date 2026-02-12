from odoo import api, fields, models
from odoo.exceptions import UserError


class Company(models.Model):
    _inherit = "res.company"

    chatwoot_account_id = fields.Char(
        string="Chatwoot Account ID",
        help="ID da conta do Chatwoot Padrão"
    )
