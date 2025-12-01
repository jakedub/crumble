from django.db import models

class Notification(models.Model):
    message = models.TextField()
    type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return getattr(self, 'name', str(self.id))
