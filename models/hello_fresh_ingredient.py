from odoo import models, fields, api

class HelloFreshIngredient(models.Model):
    _name = 'hello.fresh.ingredient'
    _description = 'Hello Fresh Recipes Lines'

    recipe_id = fields.Many2one(
        'hello.fresh.recipe',
        string='Recipe',
        ondelete='cascade'
    )

    ingredient_id = fields.Many2one(
        'product.product',
        string='Ingredient',
        required=True
    )

    quantity = fields.Float(string='Quantity', required=True)

    uom_id = fields.Many2one(
        'uom.uom',
        string='Unit of Measure',
        required=True
    )

    unit_cost = fields.Float(
        string='Unit Cost',
        compute='_compute_unit_cost',
        store=True
    )

    subtotal = fields.Float(
        string='Subtotal',
        compute='_compute_subtotal',
        store=True
    )

    @api.depends('ingredient_id')
    def _compute_unit_cost(self):
        for line in self:
            line.unit_cost = line.ingredient_id.standard_price if line.ingredient_id else 0.0

    @api.depends('unit_cost', 'quantity', 'uom_id', 'ingredient_id')
    def _compute_subtotal(self):
        for line in self:
            if line.ingredient_id and line.uom_id:
                # convert quantity to product base UoM
                converted_qty = line.uom_id._compute_quantity(
                    line.quantity, line.ingredient_id.uom_id
                )
                line.subtotal = line.unit_cost * converted_qty
            else:
                line.subtotal = 0.0

