from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import viewsets, permissions, mixins
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import AllowCreateWithoutAuthentication, IsAdminUser
from .serializers import (
    UserSerializer,
    LightSensorSerializer,
    ColorSensorSerializer,
    WaterFlowSensorSerializer,
    MoistureSensorSerializer,
    OverflowSensorSerializer,
    LeakSensorSerializer,
    LOSensorSerializer,
    ReedSwitch1Serializer,
    ReedSwitch2Serializer,
    DistanceSensorSerializer,
    CurrentSensorSerializer,
    TemperatureSensorSerializer,
    GyroscopeSerializer,
    AccelerometerSerializer,
    FanSerializer, CustomTokenObtainPairSerializer, AlertSerializer, DeviceStateSerializer
)

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status

from .models import (
    LightSensor, ColorSensor, WaterFlowSensor, MoistureSensor, OverflowSensor,
    LeakSensor, LOSensor, ReedSwitch1, ReedSwitch2, DistanceSensor,
    CurrentSensor, TemperatureSensor, Gyroscope, Accelerometer, Fan, Command
)
from .filters import (
    LightSensorFilter,
    ColorSensorFilter,
    WaterFlowSensorFilter,
    MoistureSensorFilter,
    OverflowSensorFilter,
    LeakSensorFilter,
    LOSensorFilter,
    ReedSwitch1Filter,
    ReedSwitch2Filter,
    DistanceSensorFilter,
    CurrentSensorFilter,
    TemperatureSensorFilter,
    GyroscopeFilter,
    AccelerometerFilter,
    FanFilter
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

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
# ViewSet для LightSensor
class LightSensorViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    ViewSet для управления данными датчика освещённости.
    """
    queryset = LightSensor.objects.all().order_by('-timestamp')
    serializer_class = LightSensorSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = LightSensorFilter

    @swagger_auto_schema(
        operation_description="Создание записи датчика освещённости",
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
        operation_description="Получение списка записей датчика освещённости с фильтрацией",
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


# ViewSet для ColorSensor
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


# ViewSet для WaterFlowSensor
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


# ViewSet для MoistureSensor
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


# ViewSet для OverflowSensor
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


# ViewSet для новых сенсоров

# LeakSensor
class LeakSensorViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    ViewSet для управления данными датчика протечки.
    """
    queryset = LeakSensor.objects.all().order_by('-timestamp')
    serializer_class = LeakSensorSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = LeakSensorFilter

    @swagger_auto_schema(
        operation_description="Создание записи датчика протечки",
        responses={
            201: openapi.Response("Запись успешно создана", LeakSensorSerializer),
            400: "Неверные данные"
        },
        request_body=LeakSensorSerializer,
        tags=["LeakSensor"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей датчика протечки с фильтрацией",
        responses={
            200: openapi.Response("Список записей", LeakSensorSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('min_value', openapi.IN_QUERY, description="Минимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_value', openapi.IN_QUERY, description="Максимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["LeakSensor"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# LOSensor
class LOSensorViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    """
    ViewSet для управления данными датчика ЛОС.
    """
    queryset = LOSensor.objects.all().order_by('-timestamp')
    serializer_class = LOSensorSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = LOSensorFilter

    @swagger_auto_schema(
        operation_description="Создание записи датчика ЛОС",
        responses={
            201: openapi.Response("Запись успешно создана", LOSensorSerializer),
            400: "Неверные данные"
        },
        request_body=LOSensorSerializer,
        tags=["LOSensor"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей датчика ЛОС с фильтрацией",
        responses={
            200: openapi.Response("Список записей", LOSensorSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('min_value', openapi.IN_QUERY, description="Минимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_value', openapi.IN_QUERY, description="Максимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["LOSensor"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# ReedSwitch1
class ReedSwitch1ViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    """
    ViewSet для управления данными Геркона №1.
    """
    queryset = ReedSwitch1.objects.all().order_by('-timestamp')
    serializer_class = ReedSwitch1Serializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReedSwitch1Filter

    @swagger_auto_schema(
        operation_description="Создание записи Геркона №1",
        responses={
            201: openapi.Response("Запись успешно создана", ReedSwitch1Serializer),
            400: "Неверные данные"
        },
        request_body=ReedSwitch1Serializer,
        tags=["ReedSwitch1"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей Геркона №1 с фильтрацией",
        responses={
            200: openapi.Response("Список записей", ReedSwitch1Serializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('is_triggered', openapi.IN_QUERY, description="Сработан ли геркон (true/false)", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["ReedSwitch1"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# ReedSwitch2
class ReedSwitch2ViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    """
    ViewSet для управления данными Геркона №2.
    """
    queryset = ReedSwitch2.objects.all().order_by('-timestamp')
    serializer_class = ReedSwitch2Serializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReedSwitch2Filter

    @swagger_auto_schema(
        operation_description="Создание записи Геркона №2",
        responses={
            201: openapi.Response("Запись успешно создана", ReedSwitch2Serializer),
            400: "Неверные данные"
        },
        request_body=ReedSwitch2Serializer,
        tags=["ReedSwitch2"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей Геркона №2 с фильтрацией",
        responses={
            200: openapi.Response("Список записей", ReedSwitch2Serializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('is_triggered', openapi.IN_QUERY, description="Сработан ли геркон (true/false)", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["ReedSwitch2"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# DistanceSensor
class DistanceSensorViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """
    ViewSet для управления данными датчика расстояния.
    """
    queryset = DistanceSensor.objects.all().order_by('-timestamp')
    serializer_class = DistanceSensorSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DistanceSensorFilter

    @swagger_auto_schema(
        operation_description="Создание записи датчика расстояния",
        responses={
            201: openapi.Response("Запись успешно создана", DistanceSensorSerializer),
            400: "Неверные данные"
        },
        request_body=DistanceSensorSerializer,
        tags=["DistanceSensor"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей датчика расстояния с фильтрацией",
        responses={
            200: openapi.Response("Список записей", DistanceSensorSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('min_value', openapi.IN_QUERY, description="Минимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_value', openapi.IN_QUERY, description="Максимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["DistanceSensor"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# CurrentSensor
class CurrentSensorViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """
    ViewSet для управления данными датчика тока.
    """
    queryset = CurrentSensor.objects.all().order_by('-timestamp')
    serializer_class = CurrentSensorSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CurrentSensorFilter

    @swagger_auto_schema(
        operation_description="Создание записи датчика тока",
        responses={
            201: openapi.Response("Запись успешно создана", CurrentSensorSerializer),
            400: "Неверные данные"
        },
        request_body=CurrentSensorSerializer,
        tags=["CurrentSensor"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей датчика тока с фильтрацией",
        responses={
            200: openapi.Response("Список записей", CurrentSensorSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('min_value', openapi.IN_QUERY, description="Минимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_value', openapi.IN_QUERY, description="Максимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["CurrentSensor"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# TemperatureSensor
class TemperatureSensorViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    """
    ViewSet для управления данными датчика температуры.
    """
    queryset = TemperatureSensor.objects.all().order_by('-timestamp')
    serializer_class = TemperatureSensorSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TemperatureSensorFilter

    @swagger_auto_schema(
        operation_description="Создание записи датчика температуры",
        responses={
            201: openapi.Response("Запись успешно создана", TemperatureSensorSerializer),
            400: "Неверные данные"
        },
        request_body=TemperatureSensorSerializer,
        tags=["TemperatureSensor"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей датчика температуры с фильтрацией",
        responses={
            200: openapi.Response("Список записей", TemperatureSensorSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('min_value', openapi.IN_QUERY, description="Минимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_value', openapi.IN_QUERY, description="Максимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["TemperatureSensor"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# Gyroscope
class GyroscopeViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    ViewSet для управления данными гироскопа.
    """
    queryset = Gyroscope.objects.all().order_by('-timestamp')
    serializer_class = GyroscopeSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = GyroscopeFilter

    @swagger_auto_schema(
        operation_description="Создание записи гироскопа",
        responses={
            201: openapi.Response("Запись успешно создана", GyroscopeSerializer),
            400: "Неверные данные"
        },
        request_body=GyroscopeSerializer,
        tags=["Gyroscope"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей гироскопа с фильтрацией",
        responses={
            200: openapi.Response("Список записей", GyroscopeSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('gyro_x_min', openapi.IN_QUERY, description="Минимальное значение по оси X", type=openapi.TYPE_NUMBER),
            openapi.Parameter('gyro_x_max', openapi.IN_QUERY, description="Максимальное значение по оси X", type=openapi.TYPE_NUMBER),
            openapi.Parameter('gyro_y_min', openapi.IN_QUERY, description="Минимальное значение по оси Y", type=openapi.TYPE_NUMBER),
            openapi.Parameter('gyro_y_max', openapi.IN_QUERY, description="Максимальное значение по оси Y", type=openapi.TYPE_NUMBER),
            openapi.Parameter('gyro_z_min', openapi.IN_QUERY, description="Минимальное значение по оси Z", type=openapi.TYPE_NUMBER),
            openapi.Parameter('gyro_z_max', openapi.IN_QUERY, description="Максимальное значение по оси Z", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["Gyroscope"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# Accelerometer
class AccelerometerViewSet(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    """
    ViewSet для управления данными акселерометра.
    """
    queryset = Accelerometer.objects.all().order_by('-timestamp')
    serializer_class = AccelerometerSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AccelerometerFilter

    @swagger_auto_schema(
        operation_description="Создание записи акселерометра",
        responses={
            201: openapi.Response("Запись успешно создана", AccelerometerSerializer),
            400: "Неверные данные"
        },
        request_body=AccelerometerSerializer,
        tags=["Accelerometer"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей акселерометра с фильтрацией",
        responses={
            200: openapi.Response("Список записей", AccelerometerSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('accel_x_min', openapi.IN_QUERY, description="Минимальное значение по оси X", type=openapi.TYPE_NUMBER),
            openapi.Parameter('accel_x_max', openapi.IN_QUERY, description="Максимальное значение по оси X", type=openapi.TYPE_NUMBER),
            openapi.Parameter('accel_y_min', openapi.IN_QUERY, description="Минимальное значение по оси Y", type=openapi.TYPE_NUMBER),
            openapi.Parameter('accel_y_max', openapi.IN_QUERY, description="Максимальное значение по оси Y", type=openapi.TYPE_NUMBER),
            openapi.Parameter('accel_z_min', openapi.IN_QUERY, description="Минимальное значение по оси Z", type=openapi.TYPE_NUMBER),
            openapi.Parameter('accel_z_max', openapi.IN_QUERY, description="Максимальное значение по оси Z", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["Accelerometer"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# Fan
class FanViewSet(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    """
    ViewSet для управления данными вентилятора.
    """
    queryset = Fan.objects.all().order_by('-timestamp')
    serializer_class = FanSerializer
    permission_classes = [AllowCreateWithoutAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FanFilter

    @swagger_auto_schema(
        operation_description="Создание записи вентилятора",
        responses={
            201: openapi.Response("Запись успешно создана", FanSerializer),
            400: "Неверные данные"
        },
        request_body=FanSerializer,
        tags=["Fan"],
        security=[]  # Разрешить без авторизации
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка записей вентилятора с фильтрацией",
        responses={
            200: openapi.Response("Список записей", FanSerializer(many=True))
        },
        manual_parameters=[
            openapi.Parameter('min_value', openapi.IN_QUERY, description="Минимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('max_value', openapi.IN_QUERY, description="Максимальное значение", type=openapi.TYPE_NUMBER),
            openapi.Parameter('start_date', openapi.IN_QUERY, description="Начальная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            openapi.Parameter('end_date', openapi.IN_QUERY, description="Конечная дата (ISO 8601)", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        ],
        tags=["Fan"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)



# api/views.py

import requests
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommandSerializer
from django.conf import settings

class CommandView(APIView):
    """
    Прием команд от фронтенда и отправка их на ESP-устройства.
    """
    permission_classes = [permissions.IsAuthenticated]  # Требуется аутентификация для отправки команд

    command_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'pump': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Помпа включена/выключена'),
            'led': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Лента включена/выключена'),
            'servo1': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Серво №1 включена/выключена'),
            'servo2': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Серво №2 включена/выключена'),
            'auto_light': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Авто-свет включен/выключен'),
            'brightness': openapi.Schema(type=openapi.TYPE_NUMBER, description='Яркость ленты'),
            'fan': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Вентилятор включен/выключен'),
            'ventilation': openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                          description='Режим проветривания включен/выключен'),
            'earthquake': openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                         description='Землетрясение обнаружено/не обнаружено'),
            'user_name': openapi.Schema(type=openapi.TYPE_STRING, description='Текст авторизации'),
        },
        required=['authorization']
    )

    @swagger_auto_schema(
        request_body=command_schema,
        responses={
            200: openapi.Response(
                description="Результаты отправки команд",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'results': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            additional_properties=openapi.Schema(type=openapi.TYPE_STRING)
                        )
                    }
                )
            ),
            400: openapi.Response(description="Неверные данные"),
        },
        operation_description="Отправка команд на ESP-устройства",
        tags=["Commands"],
    )
    def post(self, request, format=None):
        serializer = CommandSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            user_name = request.data.get("user_name")
            user = request.user  # Получение текущего аутентифицированного пользователя

            # Список ESP-устройств (можно вынести в настройки)
            esp_devices = settings.ESP_DEVICES

            # Формирование команд для отправки и сохранение в базе данных
            commands = {}
            for key in ['pump', 'led', 'servo1', 'servo2', 'auto_light', 'brightness', 'fan', 'ventilation', 'earthquake']:
                if key in data:
                    commands[key] = data[key]
                    # Сохранение команды в базе данных
                    Command.objects.create(
                        user=user,
                        command_type=key,
                        value=str(data[key])
                    )
            commands['user_name'] = user_name
            # Отправка команд на ESP-устройства
            results = {}
            for esp in esp_devices:
                try:
                    response = requests.post(esp, json=commands, timeout=5)
                    if response.status_code == 200:
                        results[esp] = "Success"
                    else:
                        results[esp] = f"Failed with status {response.status_code}"
                except requests.exceptions.RequestException as e:
                    results[esp] = f"Error: {str(e)}"

            return Response({"results": results}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AlertReceiveView(APIView):
    """
    Эндпоинт для приема событий от ESP-устройств.
    """
    permission_classes = [AllowAny]  # Разрешаем доступ без аутентификации

    alert_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'alert_type': openapi.Schema(type=openapi.TYPE_STRING, description='Тип события', enum=['earthquake', 'ventilation']),
            'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Состояние события'),
            'received_from': openapi.Schema(type=openapi.TYPE_STRING, description='Откуда получено событие'),
        },
        required=['alert_type', 'is_active']
    )

    @swagger_auto_schema(
        request_body=alert_schema,
        responses={
            201: openapi.Response("Событие успешно создано", AlertSerializer),
            400: "Неверные данные"
        },
        operation_description="Прием событий от ESP-устройств",
        tags=["Alerts"],
        security=[]  # Без авторизации
    )
    def post(self, request, format=None):
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            alert = serializer.save()
            # Отправка уведомления через Channels
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "alerts",  # Название группы
                {
                    "type": "alert_message",
                    "message": {
                        "alert_type": alert.get_alert_type_display(),
                        "is_active": alert.is_active,
                        "timestamp": alert.timestamp.isoformat(),
                        "received_from": alert.received_from,
                    }
                }
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceStateView(APIView):
    """
    Эндпоинт для получения текущих состояний девайсов.
    """
    permission_classes = [permissions.AllowAny]  # Настройте разрешения при необходимости

    def get(self, request, format=None):
        # Определяем типы девайсов
        device_types = ['pump', 'led', 'servo1', 'servo2', 'auto_light', 'brightness', 'fan', 'ventilation',
                        'earthquake']

        state = {}
        for device in device_types:
            latest_command = Command.objects.filter(command_type=device).order_by('-timestamp').first()
            if latest_command:
                # Обработка значений в зависимости от типа девайса
                if device == 'brightness':
                    try:
                        state[device] = float(latest_command.value)
                    except ValueError:
                        state[device] = 0.0  # Значение по умолчанию при ошибке
                else:
                    # Предполагаем, что остальные девайсы имеют булевое значение
                    state[device] = latest_command.value.lower() == 'true'
            else:
                # Значения по умолчанию, если команды еще не были отправлены
                if device == 'brightness':
                    state[device] = 0.0
                else:
                    state[device] = False
        serializer = DeviceStateSerializer(state)
        return Response(serializer.data, status=status.HTTP_200_OK)