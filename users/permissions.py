from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """Проверяет, является ли пользователь администратором."""

    message = "Доступно только модератору"

    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsAuthor(BasePermission):
    """Проверяет, является ли пользователь владельцем объекта."""

    message = "Доступно только владельцу"

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
