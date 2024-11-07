from rest_framework import permissions

"""Проверка, входит ли пользователь в группу модератороов."""
class IsModer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()
