from django.shortcuts import render
import os
from . import settings

host = os.getenv('HOST_NAME', None)
if settings.DEBUG:
    host = '127.0.0.1'

def index(request):
    context = {
        'title': 'Plow Me',
        'script_src': f'http://{host}/static/bundles/index.js',
    }
    return render(request, 'react/react.html', context)
