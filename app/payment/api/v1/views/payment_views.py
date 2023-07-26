"""
API V1: Payment Views
"""
###
# Libraries
###

from rest_framework import viewsets
from app.storage.models.storage import Storage
from app.payment.models.payment import Payment
from app.payment.api.v1.serializers.payment.default import DefaultPaymentSerializer


###
# Viewsets
###


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = DefaultPaymentSerializer
