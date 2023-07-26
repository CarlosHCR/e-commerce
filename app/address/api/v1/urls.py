"""
API V1: Address Urls
"""
###
# Libraries
###
from django.urls import path, include
from rest_framework import routers
from app.address.api.v1.views.address_views import AddressViewSet


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()

router.register(
    r'address',
    AddressViewSet,
    basename='address'
)

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
]
