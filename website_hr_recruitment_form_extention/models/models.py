from odoo import models, fields, api
# partner_name
# email_from
# partner_phone
# job_id [hidden]
# department_id [hidden]

# # Extension
# Photo
# gender (Selection)
# Nationality
# DateOfBirth
# HomeAddress
# Citizenship
# MaritalStatus
# languages
# additionalCourses
# Workplace
# Position
# StartDate
# EndDate
# StillWorking

# University
# StartDate
# EndDate

# isExperienced
# Skills


class ApplicantExtension(models.Model):
    _inherit = 'hr.applicant'

    nationality = fields.Char(string="Nationality")
    skills = fields.Text(string="Skills")
    gender = fields.Char(string="Gender")
    homeAddress = fields.Char(string="Home Address")
    citizenship = fields.Char(string="Citizenship")
    maritalStatus = fields.Char(string="Marital Status")
