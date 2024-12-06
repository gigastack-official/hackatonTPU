from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from .views import RegisterView, LightSensorViewSet, ColorSensorViewSet, WaterFlowSensorViewSet, MoistureSensorViewSet, OverflowSensorViewSet

router = routers.DefaultRouter()
router.register(r'light-sensor', LightSensorViewSet, basename='light-sensor')
router.register(r'color-sensor', ColorSensorViewSet, basename='color-sensor')
router.register(r'water-flow-sensor', WaterFlowSensorViewSet, basename='water-flow-sensor')
router.register(r'moisture-sensor', MoistureSensorViewSet, basename='moisture-sensor')
router.register(r'overflow-sensor', OverflowSensorViewSet, basename='overflow-sensor')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
