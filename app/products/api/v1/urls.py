"""
API V1: Products Urls
"""
###
# Libraries
###
from django.urls import path, include
from rest_framework import routers
from app.products.api.v1.views.products_views import ProductsViewSet


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()

router.register(
    r'products',
    ProductsViewSet,
    basename='products'
)

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
]
