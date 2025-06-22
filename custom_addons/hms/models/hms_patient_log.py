from odoo import models, fields

class PatientLog(models.Model):
    _name = 'hms.patient.log'

    patient_id = fields.Many2one('hms.patient')
    description = fields.Text()