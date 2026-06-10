from rest_framework import serializers
from apps.products.models import *


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'