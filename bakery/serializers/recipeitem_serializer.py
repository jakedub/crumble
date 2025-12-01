from rest_framework import serializers
from bakery.models.recipeitem import RecipeItem

class RecipeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeItem
        fields = '__all__'
