"""
Product Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class ProductConfig(AppConfig):
    name = 'app.product'

    def ready(self):
        import app.product.signals
