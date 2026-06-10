from rest_framework import serializers
from apps.orders.models import *

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'