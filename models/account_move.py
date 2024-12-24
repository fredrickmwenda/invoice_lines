# models/account_move.py
from odoo import models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.depends('invoice_line_ids.computed_amount')
    def _compute_amount_total(self):
        for invoice in self:
            invoice.amount_total = sum(line.computed_amount for line in invoice.invoice_line_ids)
            invoice.amount_untaxed_signed = sum(line.computed_amount for line in invoice.invoice_line_ids)
            invoice.amount_total_signed = sum(line.computed_amount for line in invoice.invoice_line_ids)
            invoice.amount_total_in_currency_signed = sum(line.computed_amount for line in invoice.invoice_line_ids)
