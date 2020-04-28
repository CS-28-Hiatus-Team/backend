from django.urls import path, include, re_path
from django.conf.urls import url
from rest_framework import routers
from api import views

# Router Patterns
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# URL Patterns
urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]
