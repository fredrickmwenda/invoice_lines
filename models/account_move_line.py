# InvoiceLines/models/account_move_line.py
from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    color = fields.Char(string="Colour")
    meters = fields.Float(string="Meters")
    vat = fields.Float(string="VAT (%)")
    discount = fields.Float(string="Discount (%)")
    computed_amount = fields.Float(string="Amount", compute="_compute_amount", store=True)


    @api.depends('meters', 'quantity', 'price_unit')
    def _compute_amount(self):
        for line in self:
            line.computed_amount = line.meters * line.quantity * line.price_unit
            line.price_subtotal = line.computed_amount

