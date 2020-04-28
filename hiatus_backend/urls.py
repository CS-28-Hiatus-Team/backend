"""hiatus_backend URL Configuration
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import include

# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
