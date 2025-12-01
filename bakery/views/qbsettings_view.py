from rest_framework import viewsets
from bakery.models.qbsettings import Settings
from bakery.serializers.qbsettings_serializer import QbSettingsSerializer


class QbSettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = QbSettingsSerializer
