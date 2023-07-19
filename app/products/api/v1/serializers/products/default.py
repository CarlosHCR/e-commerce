"""
API V1: Products Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from app.products.models.products import Product

###
# Serializers
###


class DefaultProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
