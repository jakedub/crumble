from django.db import models

class PurchaseItem(models.Model):
    purchase_order = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE, related_name='items')
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    quantity_ordered = models.DecimalField(max_digits=10, decimal_places=2)
    unit_cost_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return getattr(self, 'name', str(self.id))
