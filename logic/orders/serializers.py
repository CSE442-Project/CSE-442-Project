from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.user.username')
    cost = serializers.SerializerMethodField()

    def get_cost(self, obj):
        return obj.client.client_profile.dw_size * 15

    class Meta:
        model = models.Order
        fields = '__all__'
