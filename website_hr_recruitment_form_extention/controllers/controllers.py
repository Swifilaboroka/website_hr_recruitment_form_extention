# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteHrRecruitmentFormExtention(http.Controller):
#     @http.route('/website_hr_recruitment_form_extention/website_hr_recruitment_form_extention/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_hr_recruitment_form_extention/website_hr_recruitment_form_extention/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_hr_recruitment_form_extention.listing', {
#             'root': '/website_hr_recruitment_form_extention/website_hr_recruitment_form_extention',
#             'objects': http.request.env['website_hr_recruitment_form_extention.website_hr_recruitment_form_extention'].search([]),
#         })

#     @http.route('/website_hr_recruitment_form_extention/website_hr_recruitment_form_extention/objects/<model("website_hr_recruitment_form_extention.website_hr_recruitment_form_extention"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_hr_recruitment_form_extention.object', {
#             'object': obj
#         })
