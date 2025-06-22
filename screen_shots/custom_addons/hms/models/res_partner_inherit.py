from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    
    related_patient_id = fields.Many2one(
        'hms.patient',
        ondelete='cascade'
    )

    
    vat = fields.Char(required=True)
    
    @api.constrains('related_patient_id')
    def _check_unique_patient_email(self):
        for rec in self:
            patient = rec.related_patient_id
            if patient and patient.email:
                all_customers = self.search([
                    ('id', '!=', rec.id),
                    ('related_patient_id', '!=', False),
                ])
                for customer in all_customers:
                    if customer.related_patient_id.email == patient.email:
                        raise ValidationError(
                            "This patient is already linked to another customer with the same email."
                        )
                        
    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise ValidationError("You cannot delete a customer linked to a patient.")
        return super().unlink()
