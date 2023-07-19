"""
API V1: Products Views
"""
###
# Libraries
###

from rest_framework import viewsets
from app.products.models.products import Product
from app.storage.api.v1.serializers.storage.default import DefaultStorageSerializer


###
# Viewsets
###


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = DefaultStorageSerializer
