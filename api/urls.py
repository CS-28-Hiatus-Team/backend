
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework import routers


urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls'))
]
