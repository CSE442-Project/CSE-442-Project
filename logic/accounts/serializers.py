from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'


class ClientInfoSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    def get_address(self, obj):
        serializer = AddressSerializer(obj.address)
        return serializer.data

    class Meta:
        model = models.ClientProfile
        fields = (
            'username',
            'email',
            'phone',
            'dw_size',
            'address',
        )
