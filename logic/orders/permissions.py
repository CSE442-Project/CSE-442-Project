from rest_framework import permissions
from django.contrib.auth.models import Group


class IsClient(permissions.BasePermission):

    def has_permission(self, request, view):
        pass



class IsContractor(permissions.BasePermission):

    def has_permission(self, request, view):
        pass
