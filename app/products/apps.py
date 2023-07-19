"""
Products Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class ProductsConfig(AppConfig):
    name = 'app.products'

    def ready(self):
        import app.products.signals
