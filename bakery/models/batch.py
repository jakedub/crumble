from django.db import models

class Batch(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='batches')
    quantity_produced = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return getattr(self, 'name', str(self.id))
