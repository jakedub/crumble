from django.db import models

class Order(models.Model):
    squarespace_order_id = models.CharField(max_length=255, unique=True)
    order_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer_email = models.EmailField()
    is_synced_to_qb = models.BooleanField(default=False)
    raw_json_data = models.JSONField()

    def __str__(self):
        return getattr(self, 'name', str(self.id))
