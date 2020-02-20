from django.urls import resolve
from django.test import TestCase, Client
from django.http import HttpRequest
import os
from . import views
from logic import settings

host = os.getenv('HOST_NAME', None)
if settings.DEBUG:
    host = '127.0.0.1'

class CreateClientTest(TestCase):

    def test_create_client_resolves_to_create_client_view(self):
        found = resolve('/accounts/create/client/')
        self.assertEqual(views.create_client, found.func)

    def test_proper_template_is_used_in_view(self):
        client = Client()
        response = client.get('/accounts/create/client/')
        self.assertEqual(response.templates[0].name, 'accounts/create_client.html')


class CreateContractorTest(TestCase):

    def test_create_contractor_resolves_to_create_contractor_view(self):
        found = resolve('/accounts/create/contractor/')
        self.assertEqual(views.create_contractor, found.func)

    def test_proper_template_is_used_in_view(self):
        client = Client()
        response = client.get('/accounts/create/contractor/')
        self.assertEqual(response.templates[0].name, 'accounts/create_contractor.html')

class CreateVerification(TestCase):

    def test_create_verification_resolves_to_create_verification(self):
        found = resolve('/accounts/create/verification/')
        self.assertEqual(views.create_verification, found.func)

    def test_proper_template_is_used_in_view(self):
        client = Client()
        response = client.get('/accounts/create/verification/')
        self.assertEqual(response.templates[0].name, 'accounts/create_verification.html')
