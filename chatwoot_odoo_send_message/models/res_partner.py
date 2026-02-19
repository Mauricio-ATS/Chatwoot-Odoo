import re

from odoo import fields, models,  api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    phone_sanitized = fields.Char(
        string='Sanitized Number', compute="_compute_phone_sanitized", compute_sudo=True, store=True,
        help="Field used to store sanitized phone number. Helps speeding up searches and comparisons.")
    
    @api.depends('phone')
    def _compute_phone_sanitized(self):
        for record in self:
            phone = record.mobile or ''
            sanitized = re.sub(r'\D', '', phone)
            record.phone_sanitized = sanitized

    def action_send_msg(self):
        """Abre o wizard personalizado de WhatsApp com templates e preview."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Send WhatsApp Message'),
            'res_model': 'chatwoot.composer',  
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_partner_id': [(6, 0, [self.id])], 
                'default_model': 'res.partner',
                'default_res_id': self.id,
            },
        }
