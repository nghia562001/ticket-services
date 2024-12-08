from odoo import models, fields # type: ignore

class EventRegistration(models.Model):
    _inherit = 'event.registration'

    pickup = fields.Char(string='Pick up', translate=True)