from rest_framework.permissions import BasePermission, SAFE_METHODS


class AllowCreateWithoutAuthentication(BasePermission):
    """
    Позволяет выполнять операции создания (POST) без аутентификации,
    остальные действия требуют аутентификации.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True  # Разрешить все POST-запросы
        return request.user and request.user.is_authenticated  # Остальные запросы требуют аутентификации


class IsAdminUser(BasePermission):
    """
    Позволяет доступ только администратору.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff
