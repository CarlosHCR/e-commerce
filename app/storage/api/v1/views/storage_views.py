"""
API V1: Storage Views
"""
###
# Libraries
###

from rest_framework import viewsets
from app.storage.models.storage import Storage
from app.storage.api.v1.serializers.storage.default import DefaultStorageSerializer


###
# Viewsets
###


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = DefaultStorageSerializer
