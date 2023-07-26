###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _


###
# Model
###


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
