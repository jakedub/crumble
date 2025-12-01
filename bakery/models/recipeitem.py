from django.db import models

class RecipeItem(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='items')
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    quantity_required = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return getattr(self, 'name', str(self.id))
