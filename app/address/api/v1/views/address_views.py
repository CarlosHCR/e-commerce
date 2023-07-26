"""
API V1: Storage Views
"""
###
# Libraries
###

from rest_framework import viewsets
from app.address.models.address import Address
from app.address.api.v1.serializers.address.default import DefaultAddressSerializer


###
# Viewsets
###


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = DefaultAddressSerializer
