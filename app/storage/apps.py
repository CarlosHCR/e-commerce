"""
Storage Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class StorageConfig(AppConfig):
    name = 'app.storage'

    def ready(self):
        import app.storage.signals
