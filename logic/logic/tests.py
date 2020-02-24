from django.urls import resolve
from django.test import TestCase, Client
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

    def test_proper_template_is_used_in_view(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.templates[0].name, 'react/react.html')

    def test_proper_context_used_in_view(self):
        client = Client()
        response = client.get('/')
        context = response.context
        self.assertEqual(context['script_src'], f'http://{host}/static/bundles/index.js')
        self.assertEqual(context['title'], 'Plow Me')
