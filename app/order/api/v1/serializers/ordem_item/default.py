"""
API V1: OrderItem Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from app.order.models.order_item import OrderItem

###
# Serializers
###


class DefaultOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'
