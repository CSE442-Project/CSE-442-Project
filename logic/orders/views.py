from rest_framework import viewsets, mixins
from . import serializers, models
from . import permissions as perms
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q



def _get_forbidden_response():
    response = Response({'error': 'You are not authorized to access this content'})
    response.status_code = 403
    return response



@api_view(['POST'])
@permission_classes([perms.IsClient])
def create_order(request):
    pass



@api_view(['GET'])
@permission_classes([perms.IsClient])
def cancel_order(request, id):
    pass



@api_view(['GET'])
@permission_classes([perms.IsContractor])
def finish_order(request, id):
    pass



@api_view(['GET'])
@permission_classes([perms.IsContractor])
def accept_order(request, id):
    pass



@api_view(['GET'])
@permission_classes([perms.IsContractor])
def unclaimed_orders(request):
    pass



@api_view(['GET'])
@permission_classes([perms.IsContractor])
def scheduled_orders(request):
    pass




@api_view(['GET'])
@permission_classes([perms.IsContractor])
def finished_orders(request):
    pass




@api_view(['GET'])
@permission_classes([perms.IsContractor])
def canceled_orders(request):
    pass



@api_view(['GET'])
@permission_classes([perms.IsContractor])
def my_orders(request):
    pass
