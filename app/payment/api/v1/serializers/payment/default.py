"""
API V1: Payment Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from app.payment.models.payment import Payment

###
# Serializers
###


class DefaultPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
