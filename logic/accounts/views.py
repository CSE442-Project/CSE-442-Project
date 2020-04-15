from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from . import permissions as perms
import os
from . import views, forms, serializers
from django.forms import inlineformset_factory
from logic import settings


host = os.getenv('HOST_NAME', None)
if settings.DEBUG:
    host = '127.0.0.1'


def profile(request):
    if request.user.is_authenticated:
        if perms.IsClient().has_permission(request, None):
            return HttpResponseRedirect('/accounts/client/dashboard/')
        elif perms.IsContractor().has_permission(request, None):
            return HttpResponseRedirect('/accounts/contractor/dashboard/')
    response = HttpResponse('You do not have permission to access this page.')
    response.status_code = 403
    return response



@api_view(['GET'])
@permission_classes([perms.IsClient])
def my_info(request):
    '''Returns data about the user that is authenticated and sending this request.'''
    if perms.IsClient().has_permission(request, None):
        serializer = serializers.ClientInfoSerializer(request.user.client_profile)
    return Response(serializer.data)


def create_client(request):
    if request.method == 'POST':
        form = forms.ClientCreationForm(request.POST)
        if form.is_valid():
            form.create_client()
            return HttpResponseRedirect('/accounts/create/verification/')
    else:
        form = forms.ClientCreationForm()
    return render(request, 'accounts/create_client.html', {'form': form})


def create_contractor(request):
    if request.method == 'POST':
        form = forms.ContractorCreationForm(request.POST)
        if form.is_valid():
            form.create_contractor()
            return HttpResponseRedirect('/accounts/create/verification/')
    else:
        form = forms.ContractorCreationForm()
    return render(request, 'accounts/create_contractor.html', {'form': form})


def create_verification(request):
    return render(request, 'accounts/create_verification.html')


def client_dashboard(request):
    if request.user.is_authenticated:
        if not perms.IsClient().has_permission(request, None):
            response = HttpResponse('You do not have permission to access this page.')
            response.status_code = 403
            return response
    context = {
        'title': 'Dashboard',
        'script_src': f'http://{host}/static/bundles/client_dashboard.js',
        'auth_redirect': f'http://{host}/auth/login/?next=/accounts/client/dashboard/'
    }
    return render(request, 'react/react-auth.html', context)


def contractor_dashboard(request):
    if request.user.is_authenticated:
        if not perms.IsContractor().has_permission(request, None):
            response = HttpResponse('You do not have permission to access this page.')
            response.status_code = 403
            return response
    context = {
        'title': 'Dashboard',
        'script_src': f'http://{host}/static/bundles/contractor_dashboard.js',
        'auth_redirect': f'http://{host}/auth/login/?next=/accounts/contractor/dashboard/'
    }
    return render(request, 'react/react-auth.html', context)
