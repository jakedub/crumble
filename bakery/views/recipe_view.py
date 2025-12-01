from rest_framework import viewsets
from bakery.models.recipe import Recipe
from bakery.serializers.recipe_serializer import RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
