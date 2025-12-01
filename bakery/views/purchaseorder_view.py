from rest_framework import viewsets
from bakery.models.purchaseorder import PurchaseOrder
from bakery.serializers.purchaseorder_serializer import PurchaseOrderSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
