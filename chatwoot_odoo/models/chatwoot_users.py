import base64
import requests
import io
import mimetypes
import os
from odoo import models, fields

class ChatwootUsers(models.Model):
    _name = 'chatwoot.users'
    _description = 'Chatwoot Users'


    inbox_ids = fields.One2many(
        "chatwoot.inbox",
        "user_chat_id",
        string="Inboxes"
    )

    instance_id = fields.Many2one(
        "chatwoot.instance",
        ondelete="cascade"
    )

    code = fields.Char(
        string="Código Técnico",
        required=True,
        help="Chave usada para mapear o usuário no selection"
    )
    
    name = fields.Char(required=True)

    api_token = fields.Char(
        string="API Token",
        help="Token de acesso à API do Chatwoot"
    )

    def action_sync_inboxes(self):
        url = f"{self.instance_id.base_url}/api/v1/accounts/{self.instance_id.account_id}/inboxes"
        headers = {"api_access_token": self.api_token}

        r = requests.get(url, headers=headers, timeout=30)
        data = r.json()

        Inbox = self.env["chatwoot.inbox"]

        for inbox in data.get("payload", []):
            rec = Inbox.search([
                ("user_chat_id", "=", self.id),
                ("inbox_id", "=", inbox["id"])
            ], limit=1)

            vals = {
                "name": inbox["name"],
                "inbox_id": inbox["id"],
                "user_chat_id": self.id
            }

            if rec:
                rec.write(vals)
            else:
                Inbox.create(vals)

class ChatwootInbox(models.Model):
    _name = "chatwoot.inbox"
    _description = "Chatwoot Inbox"

    name = fields.Char(required=True)
    inbox_id = fields.Integer(required=True)
    user_chat_id = fields.Many2one(
        "chatwoot.users",
        required=True,
        ondelete="cascade"
    )
    sequence = fields.Integer(default=10)