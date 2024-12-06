from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='admin').exists()


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Разрешаем просмотр всем, создание только аутентифицированным пользователям
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Разрешаем чтение всем, изменение и удаление только автору
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user