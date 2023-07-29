"""
API V1: Order Views
"""
###
# Libraries
###

from rest_framework import viewsets
from app.order.models.order import Order
from app.order.api.v1.serializers.order.create import CreateOrderSerializer
from app.order.api.v1.serializers.order.default import DefaultOrderSerializer


###
# Viewsets
###


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateOrderSerializer
        else:
            return DefaultOrderSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
