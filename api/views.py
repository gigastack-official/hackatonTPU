from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from django.contrib.auth.models import User
from .serializers import UserSerializer, PostSerializer
from .models import Post
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import PermissionDenied
from .permissions import IsAuthorOrReadOnly

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="Регистрация нового пользователя",
        security=[],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']

    @swagger_auto_schema(
        operation_description="Получение списка постов",
        security=[{'Bearer': []}],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создание нового поста",
        security=[{'Bearer': []}],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    @swagger_auto_schema(
        operation_description="Получение поста по ID",
        security=[{'Bearer': []}],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновление поста по ID",
        security=[{'Bearer': []}],
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление поста по ID",
        security=[{'Bearer': []}],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удаление поста по ID",
        security=[{'Bearer': []}],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
