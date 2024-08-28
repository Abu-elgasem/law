from odoo import models, fields, api, _

class HearingCase(models.Model):
    _name = 'hearing.case'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hearing Case"

    scheduling_date= fields.Datetime(string="Scheduling Date")
    party_id = fields.Many2one('res.partner', string="Party")
    note = fields.Char(string="Note")
    hearing_id = fields.Many2one('case')






