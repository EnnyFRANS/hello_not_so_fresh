from openpyxl.styles.builtins import total

from odoo import models, fields, api

class HelloFreshRecipe(models.Model):
    _name = 'hello.fresh.recipe'
    _description = 'single recipes'
    _inherits = {'product.template': 'product_template_id'}
    _inherit = ['mail.thread', 'mail.activity.mixin']

    product_template_id = fields.Many2one(
        'product.template', 'Product Template',
        auto_join=True, index=True, ondelete="cascade", required=True)

    is_recipe = fields.Boolean()
    is_vegetarian = fields.Boolean()
    preparation_time = fields.Integer()
    price = fields.Float(compute ='_compute_price')
    ingredient_line_ids = fields.Many2many('product.product', string='Ingredients')
    steps = fields.Html(string='Steps to follow')

    @api.depends('ingredient_line_ids.lst_price')
    def _compute_price(self):
        for recipe in self:
            total = 0
            for ingredient in recipe.ingredient_line_ids:
                total += ingredient.lst_price
            recipe.price = total



