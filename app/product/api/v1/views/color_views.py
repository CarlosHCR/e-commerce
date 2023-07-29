"""
API V1: Color Views
"""
###
# Libraries
###

from rest_framework import viewsets, permissions
from app.product.models.color import Color
from app.product.api.v1.serializers.color.default import DefaultColorSerializer


###
# Viewsets
###


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DefaultColorSerializer
