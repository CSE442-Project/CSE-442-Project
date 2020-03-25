from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^api/create/', views.create_order),
    url(r'^api/cancel/<int:id>/', views.cancel_order),
    url(r'^api/finish/<int:id>/', views.finish_order),
    url(r'^api/accept/<int:id>/', views.accept_order),
    url(r'^api/unclaimed/', views.unclaimed_orders),
    url(r'^api/scheduled/', views.scheduled_orders),
    url(r'^api/finished/', views.finished_orders),
    url(r'^api/canceled/ ', views.canceled_orders),
    url(r'^api/', views.my_orders),
]
