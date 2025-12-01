from rest_framework import viewsets
from bakery.models.ingredient import Ingredient
from bakery.serializers.ingredient_serializer import IngredientSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
