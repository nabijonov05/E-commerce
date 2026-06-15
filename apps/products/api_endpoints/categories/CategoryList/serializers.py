from rest_framework import serializers
from apps.products.models import *


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'