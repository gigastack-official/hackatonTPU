from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from .views import RegisterView, SensorViewSet, DeviceViewSet, MeasurementViewSet, LightingModeViewSet

router = routers.DefaultRouter()
router.register(r'sensors', SensorViewSet, basename='sensor')
router.register(r'devices', DeviceViewSet, basename='device')
router.register(r'measurements', MeasurementViewSet, basename='measurement')
router.register(r'lighting-modes', LightingModeViewSet, basename='lightingmode')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
