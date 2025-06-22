from odoo import models, fields,api  

class Doctor(models.Model):
    _name = 'hms.doctor'

    first_name = fields.Char()
    last_name = fields.Char()
    image = fields.Image()

    department_ids = fields.Many2many('hms.department')
    patient_ids = fields.Many2many('hms.patient')
    
    
    
    name = fields.Char(compute='_compute_name', store=True)

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.first_name} {rec.last_name}"