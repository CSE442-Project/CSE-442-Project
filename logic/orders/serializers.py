from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.user.username')

    class Meta:
        model = models.Order
        fields = '__all__'
