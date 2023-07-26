"""
API V1: Order Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from app.order.models.order import Order

###
# Serializers
###


class DefaultOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
