# api/urls.py

from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from .views import (
    RegisterView, LightSensorViewSet, ColorSensorViewSet, WaterFlowSensorViewSet,
    MoistureSensorViewSet, OverflowSensorViewSet, LeakSensorViewSet, LOSensorViewSet,
    ReedSwitch1ViewSet, ReedSwitch2ViewSet, DistanceSensorViewSet,
    CurrentSensorViewSet, TemperatureSensorViewSet, GyroscopeViewSet,
    AccelerometerViewSet, FanViewSet, CommandView, CustomTokenObtainPairView
)

router = routers.DefaultRouter()
router.register(r'light-sensor', LightSensorViewSet, basename='light-sensor')
router.register(r'color-sensor', ColorSensorViewSet, basename='color-sensor')
router.register(r'water-flow-sensor', WaterFlowSensorViewSet, basename='water-flow-sensor')
router.register(r'moisture-sensor', MoistureSensorViewSet, basename='moisture-sensor')
router.register(r'overflow-sensor', OverflowSensorViewSet, basename='overflow-sensor')

# Регистрация новых ViewSet'ов
router.register(r'leak-sensor', LeakSensorViewSet, basename='leak-sensor')
router.register(r'lo-sensor', LOSensorViewSet, basename='lo-sensor')
router.register(r'reed-switch1', ReedSwitch1ViewSet, basename='reed-switch1')
router.register(r'reed-switch2', ReedSwitch2ViewSet, basename='reed-switch2')
router.register(r'distance-sensor', DistanceSensorViewSet, basename='distance-sensor')
router.register(r'current-sensor', CurrentSensorViewSet, basename='current-sensor')
router.register(r'temperature-sensor', TemperatureSensorViewSet, basename='temperature-sensor')
router.register(r'gyroscope', GyroscopeViewSet, basename='gyroscope')
router.register(r'accelerometer', AccelerometerViewSet, basename='accelerometer')
router.register(r'fan', FanViewSet, basename='fan')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('send-command/', CommandView.as_view(), name='send-command'),  # Новый эндпоинт
    path('', include(router.urls)),
]
