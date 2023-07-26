"""
API V1: Products Views
"""
###
# Libraries
###

from rest_framework import viewsets
from app.product.models.product import Product
from app.product.api.v1.serializers.product.default import DefaultProductSerializer


###
# Viewsets
###


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = DefaultProductSerializer
