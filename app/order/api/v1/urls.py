"""
API V1: Order Urls
"""
###
# Libraries
###
from django.urls import path, include
from rest_framework import routers
from app.storage.api.v1.views.storage_views import StorageViewSet


###
# Routers
###
""" Main router """
router = routers.SimpleRouter()

router.register(
    r'order',
    StorageViewSet,
    basename='order'
)

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
]
