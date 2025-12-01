from rest_framework import viewsets
from bakery.models.batch import Batch
from bakery.serializers.batch_serializer import BatchSerializer

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
