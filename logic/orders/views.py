from rest_framework import viewsets, mixins, status
from . import serializers, models
from . import permissions as perms
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Q



def _get_forbidden_response():
    response = Response({'error': 'You are not authorized to access this content'})
    response.status_code = 403
    return response


class CreateOrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [perms.IsClient]
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.none()

    # def create(self, request, *args, **kwargs):
    #     data = {
    #         'status': 'U',
    #         'client': request.user,
    #     }
    #     if 'comment' in request.data:
    #         data['comment'] = request.data['comment']
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)



@api_view(['GET'])
@permission_classes([perms.IsClient | IsAdminUser])
def cancel_order(request, id):
    '''Provide the id an order to have it Canceled. Only the Client that submitted
    the Order can cancel it. The Order must be in the Unclaimed state.'''
    client_profile = request.user.client_profile
    order = models.Order.objects.get(pk=id)
    if order.client != client_profile:
        return _get_forbidden_response()
    order.status = 'C'
    order.save()
    return response



@api_view(['GET'])
@permission_classes([perms.IsContractor | IsAdminUser])
def finish_order(request, id):
    '''Provide the id of the Order to mark it as Finished. Only the contractor
    that accepted the Order can finish the Order. The Order must be in the Scheduled
    state.'''
    pass



@api_view(['GET'])
@permission_classes([perms.IsContractor | IsAdminUser])
def accept_order(request, id):
    '''Provide the id of the Order to mark it as mark it as Scheduled. Only
    Contractors can accept Order, and the Order must be in the Unclaimed state.'''
    pass



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def unclaimed_orders(request):
    ''''''
    pass



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def scheduled_orders(request):
    pass




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def finished_orders(request):
    pass




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def canceled_orders(request):
    pass



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_orders(request):
    pass
