from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^create/client/', views.create_client),
    url(r'^create/contractor/', views.create_contractor),
    url(r'^create/verification/', views.create_verification),
    url(r'^client/dashboard/', views.client_dashboard),
    url(r'^contractor/dashboard/', views.contractor_dashboard),
    url(r'profile/', views.profile),
    url(r'^api/my-info/', views.my_info),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate),
]
