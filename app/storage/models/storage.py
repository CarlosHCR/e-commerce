###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _
from app.products.models.products import Product


###
# Model
###


class Storage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("Product"),
    )
    
    amount = models.IntegerField(
        verbose_name=_("Amount"),
        default=0
    )
