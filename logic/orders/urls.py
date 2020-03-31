from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'', views.CreateOrderViewSet)

urlpatterns = [
    url(r'^api/create/', include(router.urls)),
    path('api/cancel/<int:id>/', views.cancel_order),
    path('api/finish/<int:id>/', views.finish_order),
    path('api/accept/<int:id>/', views.accept_order),
    url(r'^api/unclaimed/', views.unclaimed_orders),
    url(r'^api/scheduled/', views.scheduled_orders),
    url(r'^api/finished/', views.finished_orders),
    url(r'^api/canceled/ ', views.canceled_orders),
    url(r'^api/', views.my_orders),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
