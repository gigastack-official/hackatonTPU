from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

from .permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import UserSerializer, SensorSerializer, DeviceSerializer, MeasurementSerializer, \
    LightingModeSerializer
from .models import Sensor, Device, Measurement, LightingMode
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(operation_description="Регистрация нового пользователя", security=[])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminUser]  # Только админ может менять состояние устройств


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['sensor__id']
    ordering_fields = ['timestamp']


class LightingModeViewSet(viewsets.ModelViewSet):
    queryset = LightingMode.objects.all()
    serializer_class = LightingModeSerializer
    permission_classes = [IsAdminUser]
