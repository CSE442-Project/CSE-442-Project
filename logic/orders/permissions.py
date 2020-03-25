from rest_framework import permissions
from django.contrib.auth.models import Group


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.client_profile != None
        return False


class IsContractor(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.contractor_profile != None
        return False
