from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

from .permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import (
    UserSerializer,
    SensorSerializer,
    DeviceSerializer,
    MeasurementSerializer,
    LightingModeSerializer
)
from .models import Sensor, Device, Measurement, LightingMode
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="Регистрация нового пользователя",
        tags=["Auth"],
        request_body=UserSerializer,
        responses={
            201: openapi.Response("Пользователь успешно создан", UserSerializer),
            400: "Неверные данные для создания пользователя"
        },
        security=[]  # нет авторизации для регистрации
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']

    @swagger_auto_schema(
        operation_description="Получить список всех датчиков",
        tags=["Sensors"],
        responses={200: SensorSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создать новый датчик",
        tags=["Sensors"],
        request_body=SensorSerializer,
        responses={
            201: openapi.Response("Датчик успешно создан", SensorSerializer),
            400: "Неверные данные"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получить информацию о конкретном датчике по ID",
        tags=["Sensors"],
        responses={200: SensorSerializer, 404: "Датчик не найден"}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновить информацию о датчике",
        tags=["Sensors"],
        request_body=SensorSerializer,
        responses={
            200: openapi.Response("Датчик успешно обновлен", SensorSerializer),
            400: "Неверные данные",
            404: "Датчик не найден"
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частично обновить информацию о датчике",
        tags=["Sensors"],
        request_body=SensorSerializer,
        responses={
            200: openapi.Response("Датчик успешно обновлен", SensorSerializer),
            400: "Неверные данные",
            404: "Датчик не найден"
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удалить датчик",
        tags=["Sensors"],
        responses={204: "Датчик успешно удален", 404: "Датчик не найден"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminUser]  # Только админ может менять состояние устройств

    @swagger_auto_schema(
        operation_description="Получить список устройств",
        tags=["Devices"],
        responses={200: DeviceSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # Аналогично можно добавить @swagger_auto_schema для create, retrieve, update, partial_update, destroy


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['sensor__id']
    ordering_fields = ['timestamp']

    @swagger_auto_schema(
        operation_description="Получить список измерений. Можно фильтровать по sensor__id",
        tags=["Measurements"],
        responses={200: MeasurementSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                name='sensor__id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='ID датчика для фильтрации измерений'
            ),
            openapi.Parameter(
                name='ordering',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Параметры для сортировки, например ?ordering=timestamp'
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class LightingModeViewSet(viewsets.ModelViewSet):
    queryset = LightingMode.objects.all()
    serializer_class = LightingModeSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_description="Получить список режимов освещения",
        tags=["LightingModes"],
        responses={200: LightingModeSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
