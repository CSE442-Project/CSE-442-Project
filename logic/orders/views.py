from rest_framework import viewsets, mixins, status
from . import serializers, models
from . import permissions as perms
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Q



def _get_forbidden_response():
    response = Response({'message': 'You are not authorized to access this content'})
    response.status_code = 403
    return response


class CreateOrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [perms.IsClient]
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.none()

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)



@api_view(['GET'])
@permission_classes([perms.IsClient])
def cancel_order(request, id):
    '''Provide the id an order to have it Canceled. Only the Client that submitted
    the Order can cancel it. The Order must be in the Unclaimed state.'''
    order = models.Order.objects.get(pk=id)
    if order.client != request.user:
        return _get_forbidden_response()
    if order.status != 'U':
        response = Response({'message': 'Only Unclaimed Order can be canceled.'})
        response.status_code = 406
    order.status = 'C'
    order.save()
    serializer = serializers.OrderSerializer(order, context={'request': request})
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([perms.IsContractor])
def finish_order(request, id):
    '''Provide the id of the Order to mark it as Finished. Only the contractor
    that accepted the Order can finish the Order. The Order must be in the Scheduled
    state.'''
    order = models.Order.objects.get(pk=id)
    if order.contractor != request.user:
        return _get_forbidden_response()
    if order.status != 'S':
        response = Response({'message': 'Only Scheduled Order can be Finished.'})
        response.status_code = 406
    order.status= 'F'
    order.save()
    serializer = serializers.OrderSerializer(order, context={'request': request})
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([perms.IsContractor])
def accept_order(request, id):
    '''Provide the id of the Order to mark it as mark it as Scheduled. Only
    Contractors can accept Order, and the Order must be in the Unclaimed state.'''
    order = models.Order.objects.get(pk=id)
    if order.contractor != None:
        return _get_forbidden_response()
    if order.status != 'U':
        response = Response({'message': 'Only Unclaimed Order can be accepted.'})
        response.status_code = 406
    order.status = 'S'
    order.contractor = request.user
    order.save()
    serializer = serializers.OrderSerializer(order, context={'request': request})
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([perms.IsClient | perms.IsContractor])
def unclaimed_orders(request):
    '''If the User is a client, return a list of all the Order belonging to the
    client that are Unclaimed in status. If the User is a Contractor, return
    all of the Unclaimed Orders that are available for the contractor to accept'''
    if perms.IsClient().has_permission(request, None):
        orders = models.Order.objects.filter(client=request.user).filter(status='U').order_by('created_at')
    elif perms.IsContractor().has_permission(request, None):
        orders = models.Order.objects.filter(status='U').order_by('created_at')
    serializer = serializers.OrderSerializer(orders, many=True, context={'request', request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([perms.IsClient | perms.IsContractor])
def scheduled_orders(request):
    '''Return the list of all the Scheduled Orders that the user is attached to
    as either a client or a contractor.'''
    if perms.IsClient().has_permission(request, None):
        orders = models.Order.objects.filter(client=request.user).filter(status='S').order_by('created_at')
    elif perms.IsContractor().has_permission(request, None):
        orders = models.Order.objects.filter(contractor=request.user).filter(status='S').order_by('created_at')
    serializer = serializers.OrderSerializer(orders, many=True, context={'request', request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([perms.IsClient | perms.IsContractor])
def finished_orders(request):
    '''Return the list of all the Finished Orders that the user is attached to
    as either a client or a contractor.'''
    if perms.IsClient().has_permission(request, None):
        orders = models.Order.objects.filter(client=request.user).filter(status='F').order_by('created_at')
    elif perms.IsContractor().has_permission(request, None):
        orders = models.Order.objects.filter(contractor=request.user).filter(status='F').order_by('created_at')
    serializer = serializers.OrderSerializer(orders, many=True, context={'request', request})
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([perms.IsClient])
def canceled_orders(request):
    '''Return a list of all the orders that a client has canceled'''
    orders = models.Order.objects.filter(client=request.user).filter(status='C').order_by('created_at')
    serializer = serializers.OrderSerializer(orders, many=True, context={'request', request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([perms.IsClient | perms.IsContractor])
def my_orders(request):
    '''Return all of the Order regardless of status that the user is attached to
    as either a client or a contractor'''
    if perms.IsClient().has_permission(request, None):
        orders = models.Order.objects.filter(client=request.user).order_by('created_at')
    elif perms.IsContractor().has_permission(request, None):
        orders = models.Order.objects.filter(contractor=request.user).order_by('created_at')
    serializer = serializers.OrderSerializer(orders, many=True, context={'request', request})
    return Response(serializer.data)
