"""
API V1: Address Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from app.address.models.address import Address

###
# Serializers
###


class CreateAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'street', 'number', 'extra',
                  'neighborhood', 'city', 'state', 'zip_code',)
