# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MilageEntryLine(models.Model):
    _name = 'vehicle.milage_entry_line'
    _description = 'vehicle.milage_entry_line'

    date = fields.Date()
    miles = fields.Float()
    vehicle_id = fields.Many2one(comodel_name="vehicle.vehicle")
    milage_type = fields.Many2one(comodel_name="vehicle.milage_entry_line_tag")
    customer = fields.Many2one(comodel_name="res.partner", compute="_on_sale_change",
        store=True, readonly=False)
    sale_id = fields.Many2one(comodel_name="sale.order",  compute="_on_move_id_change",
        store=True, readonly=False)
    move_id = fields.Many2one(comodel_name="stock.move", compute="_on_customer_change",
        store=True, readonly=False)
    customer_readonly = fields.Boolean(default=False)
    sale_id_readonly = fields.Boolean(default=False)
    move_id_readonly = fields.Boolean(default=False)

    @api.depends('sale_id')
    def _on_sale_change(self):
        if self.sale_id:
            self.customer = self.sale_id.partner_id
        sale_contains_move = False
        for m in self.sale_id.picking_ids:
            if m.id == self.move_id.id:
                sale_contains_move = True
                break
        if not sale_contains_move:
            self.move_id = None

    @api.depends('customer')
    def _on_customer_change(self):
        if self.sale_id and (self.sale_id.partner_id.id != self.customer.id):
            self.sale_id = None
        if self.move_id and (self.move_id.partner_id.id != self.customer.id):
            self.move_id = None

    @api.depends('move_id')
    def _on_move_id_change(self):
        if self.move_id and self.move_id.sale_line_id:
            if self.move_id.sale_line_id:
                self.sale_id = self.move_id.sale_line_id.order_id
            else:
                self.sale_id.id = None
            self.customer = self.move_id.partner_id
        elif self.move_id:
            self.sale_id = None
            self.customer = self.move_id.order_partner_id
            
