"""
Payment Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class PaymentConfig(AppConfig):
    name = 'app.payment'

    def ready(self):
        import app.payment.signals
