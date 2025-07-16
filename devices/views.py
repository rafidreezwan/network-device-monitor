from django.shortcuts import render

from django.shortcuts import render
from .models import NetworkDevice


def dashboard(request):
    devices = NetworkDevice.objects.all()
    return render(request, "devices/dashboard.html", {"devices": devices})
