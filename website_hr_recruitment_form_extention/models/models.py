from odoo import models, fields, api


class ApplicantExtension(models.Model):
    _inherit = 'hr.applicant'

    gender = fields.Char(string="Gender")
    photo = fields.Image(string="Profile Photo")

    nationality = fields.Char(string="Nationality")
    dateOfBirth = fields.Date(string="Date of Brith")
    homeAddress = fields.Char(string="Home Address")
    citizenship = fields.Char(string="Citizenship")
    maritalStatus = fields.Char(string="Marital Status")
    languages = fields.Text(string="Languages")
    additionalCourses = fields.Text(string="Additional Courses")
    organization = fields.Char(string="Organization")

    hasExperience = fields.Boolean(string="Has work experience?")
    position = fields.Char(string="Postition")
    workStart = fields.Date(string="Work start date")
    workEnd = fields.Date(string="Work end date")
    stillWorking = fields.Boolean("Still working?")

    university = fields.Char(string="University")
    specialization = fields.Char(string="Specialization")
    universityStart = fields.Date(string="University start date")
    universityEnd = fields.Date(string="University end date")
    skills = fields.Text(string="Skills")
