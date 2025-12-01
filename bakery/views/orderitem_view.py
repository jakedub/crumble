from rest_framework import viewsets
from bakery.models.orderitem import OrderItem
from bakery.serializers.orderitem_serializer import OrderItemSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
