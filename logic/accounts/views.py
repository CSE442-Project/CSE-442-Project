from django.shortcuts import render
from django.http import HttpResponseRedirect
import os
from . import views, forms, models
from django.forms import inlineformset_factory


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


def get_contractor(request):
    if request.method == 'GET':
        model = models.ContractorProfile(request.GET)
        count = 0;
        conts = "Names: "
        while model.is_valid() and count < 5:
            conts = conts + " | " + (model.__str__())
        return conts
    else :
        return "Sorry there are no contractors"
