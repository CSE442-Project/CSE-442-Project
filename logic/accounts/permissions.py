from rest_framework import permissions
from django.contrib.auth.models import Group


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):
        allowed_group = Group.objects.get_or_create(name='client')[0]
        user_groups = request.user.groups.all()
        authenticated = request.user.is_authenticated
        if (authenticated and allowed_group in user_groups):
            return True
        return False


class IsContractor(permissions.BasePermission):

    def has_permission(self, request, view):
        allowed_group = Group.objects.get_or_create(name='contractor')[0]
        user_groups = request.user.groups.all()
        authenticated = request.user.is_authenticated
        if (authenticated and allowed_group in user_groups):
            return True
        return False
