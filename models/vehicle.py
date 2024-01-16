from odoo import models, fields, api, _
import datetime


class vehicle(models.Model):
    _name = 'vehicle.vehicle'
    _description = 'vehicle.vehicle'

    name = fields.Char()
    milage_entry_line_ids = fields.One2many(comodel_name="vehicle.milage_entry_line",
        inverse_name="vehicle_id")
    milage_count_in_range = fields.Float(compute="_compute_milage_count_in_range")
    milage_count = fields.Float(compute="_compute_milage_count")
    start_date = fields.Date()
    end_date = fields.Date()
 
    def action_milage_entries_in_range(self):
        milage_entries = []
        for ln in self.milage_entry_line_ids:
            if (not self.start_date) and (not self.end_date):
                milage_entries.append(ln.id)
            elif (not self.end_date) and (ln.date >= self.start_date):
                milage_entries.append(ln.id)
            elif (ln.date) and (ln.date >= self.start_date) and (ln.date <= self.end_date):
                milage_entries.append(ln.id)
        return{
            'name': _("Milage Entries"),
            'type': 'ir.actions.act_window',
            'res_model': 'vehicle.milage_entry_line',
            'view_mode': 'tree',
            'domain': [('id', 'in', milage_entries)],
        }

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

    @api.onchange('start_date', 'end_date')
    def _compute_milage_count_in_range(self):
        for vhcl in self:
            total = 0.0
            for line in vhcl.milage_entry_line_ids:
                if (not vhcl.start_date) and (not vhcl.end_date):
                    total = total + line.miles
                elif (not vhcl.end_date) and (line.date >= vhcl.start_date):
                    total = total + line.miles
                elif (line.date) and (line.date >= vhcl.start_date) and (line.date <= vhcl.end_date):
                    total = total + line.miles
            vhcl.milage_count_in_range = total
    
    @api.onchange('start_date', 'end_date')
    def _compute_milage_count(self):
        for vhcl in self:
            total = 0.0
            for line in vhcl.milage_entry_line_ids:
                total = total + line.miles
            vhcl.milage_count = total
