"""
API V1: Size Views
"""
###
# Libraries
###

from rest_framework import viewsets, permissions
from app.product.models.size import Size
from app.product.api.v1.serializers.size.default import DefaultSizeSerializer


###
# Viewsets
###


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DefaultSizeSerializer
