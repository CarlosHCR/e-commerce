"""
Accounts Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class AccountsConfig(AppConfig):
    name = 'app.accounts'

    def ready(self):
        import app.accounts.signals
