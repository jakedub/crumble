from django.db import models

class Recipe(models.Model):
    product = models.OneToOneField('Product', on_delete=models.CASCADE, related_name='recipe')
    batch_yield_qty = models.DecimalField(max_digits=10, decimal_places=2)
    batch_yield_unit = models.CharField(max_length=50)

    def __str__(self):
        return getattr(self, 'name', str(self.id))
