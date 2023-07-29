"""
API V1: OrderItem Views
"""
###
# Libraries
###

from rest_framework import viewsets, permissions
from app.order.models.order_item import OrderItem
from app.order.api.v1.serializers.ordem_item.default import DefaultOrderItemSerializer


###
# Viewsets
###


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DefaultOrderItemSerializer