"""
Order Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class OrderConfig(AppConfig):
    name = 'app.order'

    def ready(self):
        import app.order.signals
