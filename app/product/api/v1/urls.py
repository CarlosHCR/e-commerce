"""
API V1: Product Urls
"""
###
# Libraries
###
from django.urls import path, include
from rest_framework import routers
from app.product.api.v1.views.product_views import ProductViewSet


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()

router.register(
    r'product',
    ProductViewSet,
    basename='product'
)

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
]
