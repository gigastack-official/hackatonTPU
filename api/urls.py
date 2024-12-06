from django.urls import path
from .views import (
    RegisterView,
    PostListCreateView,
    PostRetrieveUpdateDestroyView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/', PostListCreateView.as_view(), name='posts_list_create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post_detail'),
]
