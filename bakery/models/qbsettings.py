from django.db import models


class QbSettings(models.Model):
    qb_access_token = models.CharField(max_length=500)
    qb_refresh_token = models.CharField(max_length=500)
    qb_realm_id = models.CharField(max_length=255)
    last_sync_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return getattr(self, "name", str(self.id))
