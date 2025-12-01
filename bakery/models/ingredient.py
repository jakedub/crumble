from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, related_name='ingredients')
    unit_of_measure = models.CharField(max_length=50)
    quantity_on_hand = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    reorder_point = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    avg_unit_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return getattr(self, 'name', str(self.id))
