###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _
from app.storage.models.storage import Storage


###
# Model
###

class OrderItem(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    amount = models.IntegerField(
        verbose_name=_("Amount"),
        default=0,
    )
