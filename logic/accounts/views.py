from django.shortcuts import render
import os
from . import views


def create_client(request):
    return render(request, 'accounts/create_client.html')


def create_contractor(request):
    return render(request, 'accounts/create_contractor.html')


def create_verification(request):
    return render(request, 'accounts/create_verification.html')
