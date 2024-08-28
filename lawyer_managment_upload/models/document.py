from odoo import fields, models, api

class Document(models.Model):
    _name = 'document'
    _description = 'Document'

    name = fields.Char(string="Document Name", required=True)
    file = fields.Binary(string="File")
    custom_model_id = fields.Many2one('case', string="Custom Model", ondelete='cascade')