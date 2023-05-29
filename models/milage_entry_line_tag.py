# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MilageEntryLineTag(models.Model):
    _name = 'vehicle.milage_entry_line_tag'
    _description = 'vehicle.milage_entry_line_tag'

    name = fields.Char()