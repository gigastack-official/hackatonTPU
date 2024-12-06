from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import (
    UserSerializer,
)

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

