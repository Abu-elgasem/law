from odoo import api,models,fields

class InheritProductTemplate(models.Model):
    _inherit = 'product.template'

    # create check in product variants "pruduct variants page"
    required_case = fields.Boolean(string='Required Case')


