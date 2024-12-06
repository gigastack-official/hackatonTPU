from rest_framework import viewsets, permissions, mixins
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import AllowCreateWithoutAuthentication, IsAdminUser
from .serializers import (
    UserSerializer,
    LightSensorSerializer,
    ColorSensorSerializer,
    WaterFlowSensorSerializer,
    MoistureSensorSerializer,
    OverflowSensorSerializer
)

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status

from .models import LightSensor, ColorSensor, WaterFlowSensor, MoistureSensor, OverflowSensor
from .filters import (
    LightSensorFilter,
    ColorSensorFilter,
    WaterFlowSensorFilter,
    MoistureSensorFilter,
    OverflowSensorFilter
)


class RegisterView(generics.CreateAPIView):
    """
    Регистрация нового пользователя.
    """
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
        security=[]  # Нет авторизации для регистрации
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LightSensorViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    ViewSet для управления данными датчика света.
    """
    queryset = LightSensor.objects.all().order_by('-timestamp')
    serializer_class = LightSensorSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = LightSensorFilter

    @swagger_auto_schema(
        operation_description="Создание записи датчика света",
        responses={
            201: openapi.Response("Запись успешно создана", LightSensorSerializer),
            400: "Неверные данные"
        },
        request_body=LightSensorSerializer,
        tags=["LightSensor"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей датчика света с фильтрацией",
        responses={
            200: openapi.Response("Список записей", LightSensorSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('min_value', openapi.IN_QUERY, description="Минимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_value', openapi.IN_QUERY, description="Максимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["LightSensor"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ColorSensorViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    ViewSet для управления данными датчика цвета.
    """
    queryset = ColorSensor.objects.all().order_by('-timestamp')
    serializer_class = ColorSensorSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ColorSensorFilter

    @swagger_auto_schema(
        operation_description="Создание записи датчика цвета",
        responses={
            201: openapi.Response("Запись успешно создана", ColorSensorSerializer),
            400: "Неверные данные"
        },
        request_body=ColorSensorSerializer,
        tags=["ColorSensor"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей датчика цвета с фильтрацией",
        responses={
            200: openapi.Response("Список записей", ColorSensorSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('min_value', openapi.IN_QUERY, description="Минимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_value', openapi.IN_QUERY, description="Максимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('is_detected', openapi.IN_QUERY, description="Обнаружен ли цвет (true/false)", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["ColorSensor"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class WaterFlowSensorViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    """
    ViewSet для управления данными датчика потока воды.
    """
    queryset = WaterFlowSensor.objects.all().order_by('-timestamp')
    serializer_class = WaterFlowSensorSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = WaterFlowSensorFilter

    @swagger_auto_schema(
        operation_description="Создание записи датчика потока воды",
        responses={
            201: openapi.Response("Запись успешно создана", WaterFlowSensorSerializer),
            400: "Неверные данные"
        },
        request_body=WaterFlowSensorSerializer,
        tags=["WaterFlowSensor"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей датчика потока воды с фильтрацией",
        responses={
            200: openapi.Response("Список записей", WaterFlowSensorSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('min_value', openapi.IN_QUERY, description="Минимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_value', openapi.IN_QUERY, description="Максимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["WaterFlowSensor"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class MoistureSensorViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    """
    ViewSet для управления данными датчика влаги.
    """
    queryset = MoistureSensor.objects.all().order_by('-timestamp')
    serializer_class = MoistureSensorSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MoistureSensorFilter

    @swagger_auto_schema(
        operation_description="Создание записи датчика влаги",
        responses={
            201: openapi.Response("Запись успешно создана", MoistureSensorSerializer),
            400: "Неверные данные"
        },
        request_body=MoistureSensorSerializer,
        tags=["MoistureSensor"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей датчика влаги с фильтрацией",
        responses={
            200: openapi.Response("Список записей", MoistureSensorSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('min_value', openapi.IN_QUERY, description="Минимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_value', openapi.IN_QUERY, description="Максимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["MoistureSensor"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class OverflowSensorViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """
    ViewSet для управления данными о переполнении.
    """
    queryset = OverflowSensor.objects.all().order_by('-timestamp')
    serializer_class = OverflowSensorSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OverflowSensorFilter

    @swagger_auto_schema(
        operation_description="Создание записи о переполнении",
        responses={
            201: openapi.Response("Запись успешно создана", OverflowSensorSerializer),
            400: "Неверные данные"
        },
        request_body=OverflowSensorSerializer,
        tags=["OverflowSensor"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей о переполнении с фильтрацией",
        responses={
            200: openapi.Response("Список записей", OverflowSensorSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('is_overflow', openapi.IN_QUERY, description="Переполнено ли (true/false)", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["OverflowSensor"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
