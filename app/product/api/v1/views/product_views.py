"""
API V1: Products Views
"""
###
# Libraries
###

from rest_framework import viewsets, permissions
from app.product.models.product import Product
from app.product.api.v1.serializers.product.default import DefaultProductSerializer
from app.product.api.v1.serializers.product.create import CreateProductSerializer


###
# Viewsets
###


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProductSerializer
        else:
            return DefaultProductSerializer
