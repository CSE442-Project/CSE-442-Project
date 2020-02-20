from django.urls import resolve
from django.test import TestCase
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


class CreateContractorTest(TestCase):

    def test_create_contractor_resolves_to_create_contractor_view(self):
        found = resolve('/accounts/create/contractor/')
        self.assertEqual(views.create_contractor, found.func)
