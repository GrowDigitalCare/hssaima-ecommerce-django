from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    
    # images = ProductImgSerializer(many=True)

    class Meta:
        model = ProductModel
        fields = '__all__'
