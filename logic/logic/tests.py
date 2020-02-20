from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
import os
from . import views
from . import settings

host = os.getenv('HOST_NAME', None)
if settings.DEBUG:
    host = '127.0.0.1'

class IndexTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(views.index, found.func)
