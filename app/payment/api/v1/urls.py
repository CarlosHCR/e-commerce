"""
API V1: Payment Urls
"""
###
# Libraries
###
from django.urls import path, include
from rest_framework import routers
from app.payment.api.v1.views.payment_views import PaymentViewSet


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()

router.register(
    r'payment',
    PaymentViewSet,
    basename='payment'
)

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
]
