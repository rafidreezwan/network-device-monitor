from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import NetworkDevice


class NetworkDeviceTestCase(TestCase):
    def setUp(self):
        NetworkDevice.objects.create(name="Test Router", ip_address="192.168.0.1")

    def test_device_creation(self):
        device = NetworkDevice.objects.get(name="Test Router")
        self.assertEqual(device.status, "Unknown")
