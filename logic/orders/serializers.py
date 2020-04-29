from django.contrib.auth.models import User
from rest_framework import serializers
from . import models
from accounts.serializers import AddressSerializer


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.username')
    contractor = serializers.ReadOnlyField(source='contractor.username')
    cost = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    navigate_url = serializers.SerializerMethodField()

    def get_cost(self, obj):
        return obj.client.client_profile.dw_size * 15

    def get_address(self, obj):
        address = obj.client.client_profile.address
        serializer = AddressSerializer(address)
        return serializer.data

    def navigate_url(self, obj):
        return f'https://www.google.com/maps/dir/?api=1&destination={str(obj.address)}'

    class Meta:
        model = models.Order
        fields = (
            'id',
            'status',
            'created_at',
            'schedule_time',
            'contractor',
            'client',
            'comment',
            'cost',
            'address',
            'navigate_url',
        )
