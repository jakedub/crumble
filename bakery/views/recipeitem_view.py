from rest_framework import viewsets
from bakery.models.recipeitem import RecipeItem
from bakery.serializers.recipeitem_serializer import RecipeItemSerializer

class RecipeItemViewSet(viewsets.ModelViewSet):
    queryset = RecipeItem.objects.all()
    serializer_class = RecipeItemSerializer
