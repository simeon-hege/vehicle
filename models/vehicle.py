# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class vehicle(models.Model):
    _name = 'vehicle.vehicle'
    _description = 'vehicle.vehicle'

    name = fields.Char()
    milage_entry_line_ids = fields.One2many(comodel_name="vehicle.milage_entry_line",
        inverse_name="vehicle_id")

    def action_milage_entries(self):
        milage_entries = []
        for ln in self.milage_entry_line_ids:
            milage_entries.append(ln.id)
        return{
            'name': _("Milage Entries"),
            'type': 'ir.actions.act_window',
            'res_model': 'vehicle.milage_entry_line',
            'view_mode': 'tree',
            'domain': [('id', 'in', milage_entries)],
        }