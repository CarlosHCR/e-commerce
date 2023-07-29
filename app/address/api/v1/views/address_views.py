"""
API V1: Address Views
"""
###
# Libraries
###

from rest_framework import viewsets, permissions
from app.address.models.address import Address
from app.address.api.v1.serializers.address.default import DefaultAddressSerializer
from app.address.api.v1.serializers.address.create import CreateAddressSerializer


###
# Viewsets
###


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateAddressSerializer
        else:
            return DefaultAddressSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
