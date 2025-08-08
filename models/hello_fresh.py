from odoo import models, fields, api

class HelloFresh(models.Model):
    _name = "hello.fresh"
    _description = "food.delivery.service"

    order_name = fields.Char(string='order name')

    # client = fields.Many2many(
    #     'res.partner',
    #     string='Client',
    #     domain="[('is_company','=', False),('category_id.name','=', 'Client')]",
    # )

    # employee = fields.Many2many(
    #     'res.partner',
    #     string='Employee',
    #     domain="[('tags','=', 'employees')]",
    # )


