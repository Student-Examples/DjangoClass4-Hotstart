from rest_framework.permissions import BasePermission


secret_key = "some_secret"


class MyTokenPermission(BasePermission):
    def has_permission(self, request, view):
        token = request.META.get("HTTP_AUTHORIZATION", "")
        return token == secret_key
