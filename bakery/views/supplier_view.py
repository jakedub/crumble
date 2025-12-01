from rest_framework import viewsets
from bakery.models.supplier import Supplier
from bakery.serializers.supplier_serializer import SupplierSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
