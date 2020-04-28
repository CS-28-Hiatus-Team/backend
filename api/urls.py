
from django.urls import path, include, re_path
from rest_framework.authtoken import views
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, RoomViewSet, PlayerViewSet

# TODO: break out router for adv views to another app
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('rooms/', RoomViewSet),
    path('players/', PlayerViewSet)
]
