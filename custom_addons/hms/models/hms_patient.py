from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError
from datetime import date


class Patient(models.Model):
    _name = 'hms.patient'

    first_name = fields.Char()
    last_name = fields.Char()
    email = fields.Char()
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O'),
    ])
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'), 
        ('serious', 'Serious'),
    ],required=True)

    pcr = fields.Boolean()
    image = fields.Image()
    address = fields.Text()
    age = fields.Integer(string="Age", compute="_compute_age", store=True, readonly=True)

    department_id = fields.Many2one('hms.department')
    department_capacity = fields.Integer(related='department_id.capacity')
    doctor_ids = fields.Many2many('hms.doctor')
    
    
    
    log_ids = fields.One2many('hms.patient.log', 'patient_id')
    def create_log(self):
        for rec in self:
            self.env['hms.patient.log'].create({
                'patient_id': rec.id,
                'description': f"State changed to {rec.state}",
            })

    def write(self, vals):
        res = super(Patient, self).write(vals)
        if 'state' in vals:
            for rec in self:
                rec.create_log()
        return res


    @api.onchange('age')
    def _onchange_age_check_pcr(self):
        if self.age and self.age < 30:
            self.pcr = True
            return {
                'warning': {
                    'title': "PCR Checked Automatically",
                    'message': "Hey! PCR is now checked! as you set the age to lower than 30",
                }
            }

    @api.constrains('email')
    def _check_valid_and_unique_email(self):
        for rec in self:
            if rec.email:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", rec.email):
                    raise ValidationError("Invalid email format.")
                
                existing = self.search([
                    ('email', '=', rec.email),
                    ('id', '!=', rec.id)
                ])
                if existing:
                    raise ValidationError("Email must be unique.")
                    
                    
    name = fields.Char(compute='_compute_name', store=True)
    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.first_name or ''} {rec.last_name or ''}".strip()
            
            

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                    (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day)
                )
            else:
                rec.age = 0





