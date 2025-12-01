from rest_framework import viewsets
from bakery.models.purchaseitem import PurchaseItem
from bakery.serializers.purchaseitem_serializer import PurchaseItemSerializer

class PurchaseItemViewSet(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer
