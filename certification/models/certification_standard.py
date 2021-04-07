from odoo import models, fields

class CertificationStandard(models.Model):
    _name='certification.standard'
    _description='Certification Types'

    name = fields.Char()
    description = fields.Text()

