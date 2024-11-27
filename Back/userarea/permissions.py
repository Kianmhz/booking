from rest_framework.permissions import BasePermission

from .functions import get_user_by_token


class AllowAnyUser(BasePermission):
    def has_permission(self, request, view):
        return True


class IsAuthenticatedUser(BasePermission):
    message = {"detail": ['You must be logged in'], 'status': 401}

    def has_permission(self, request, view):
        return get_user_by_token(request)
