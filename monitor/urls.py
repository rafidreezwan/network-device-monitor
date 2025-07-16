from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("devices.urls")),  # Use the app-level URLs for the dashboard
]
