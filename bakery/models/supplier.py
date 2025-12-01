from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    lead_time_days = models.IntegerField(default=0)

    def __str__(self):
        return getattr(self, 'name', str(self.id))
