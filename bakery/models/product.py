from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    squarespace_id = models.CharField(max_length=255, unique=True)
    inventory_on_hand = models.IntegerField(default=0)

    def __str__(self):
        return getattr(self, 'name', str(self.id))
