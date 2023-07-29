"""
API V1: Order Urls
"""
###
# Libraries
###
from django.urls import path, include
from rest_framework import routers
from app.order.api.v1.views.order_views import OrderViewSet
from app.order.api.v1.views.order_item_views import OrderItemViewSet


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()

router.register(
    r'order',
    OrderViewSet,
    basename='order'
)

router.register(
    r'order_item',
    OrderItemViewSet,
    basename='order_item'
)

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
]
