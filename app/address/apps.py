"""
Address Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class AddressConfig(AppConfig):
    name = 'app.address'

    def ready(self):
        import app.address.signals
