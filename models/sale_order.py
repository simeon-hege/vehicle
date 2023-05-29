from odoo import models, fields, api, _
import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def enter_vehicle_milage(self):
        dt = datetime.date.today()
        ctx = {
            'default_sale_id': self.id,
            'default_date': dt,
            'default_customer_readonly': True,
            'default_sale_id_readonly': True,
            'default_move_id_readonly': True, 
        }
        return{
            'name': _('Enter Vehicle Milage'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'target': 'new',
            'res_model': 'vehicle.milage_entry_line',
            'view_id': self.env.ref('vehicle.milage_form_view').id,
            'context': ctx,
        }