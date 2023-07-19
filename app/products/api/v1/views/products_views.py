"""
API V1: Products Views
"""
###
# Libraries
###

from rest_framework import viewsets
from app.products.models.products import Product
from app.products.api.v1.serializers.products.default import DefaultProductsSerializer


###
# Viewsets
###


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = DefaultProductsSerializer
