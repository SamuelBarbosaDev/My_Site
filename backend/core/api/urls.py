from rest_framework import routers
from django.urls import path, include
from api.views import (
    UserViewSet,
    GroupViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'group', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]