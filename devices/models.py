from django.db import models


class NetworkDevice(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    status = models.CharField(max_length=20, default="Unknown")
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.ip_address})"
