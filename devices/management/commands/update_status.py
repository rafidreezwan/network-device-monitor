from django.core.management.base import BaseCommand
from devices.models import NetworkDevice
import random


class Command(BaseCommand):
    help = "Mock update device statuses"

    def handle(self, *args, **kwargs):
        statuses = ["Online", "Offline", "Unreachable", "Degraded"]
        for device in NetworkDevice.objects.all():
            device.status = random.choice(statuses)
            device.save()
        self.stdout.write(self.style.SUCCESS("Device statuses updated."))
