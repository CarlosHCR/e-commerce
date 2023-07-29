"""
API V1: Product Urls
"""
###
# Libraries
###
from django.urls import path, include
from rest_framework import routers
from app.product.api.v1.views.product_views import ProductViewSet
from app.product.api.v1.views.color_views import ColorViewSet
from app.product.api.v1.views.size_views import SizeViewSet


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
router.register(
    r'color',
    ColorViewSet,
    basename='color'
)
router.register(
    r'size',
    SizeViewSet,
    basename='size'
)

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
]
