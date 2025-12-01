from django.db import models

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateField()
    total_cost = models.DecimalField(max_digits=12, decimal_places=2)
    qb_expense_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return getattr(self, 'name', str(self.id))
