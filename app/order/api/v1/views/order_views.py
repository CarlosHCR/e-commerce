"""
API V1: Order Views
"""
###
# Libraries
###

from rest_framework import viewsets
from app.order.models.order import Order
from app.order.api.v1.serializers.order.default import DefaultOrderSerializer


###
# Viewsets
###


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = DefaultOrderSerializer
