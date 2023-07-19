"""
API V1: Storage Urls
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
    r'storage',
    StorageViewSet,
    basename='storage'
)

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
]
