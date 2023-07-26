###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _
from app.product.models.product import Product


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
    size = models.CharField(
        max_length=10,
        verbose_name=_('size'),
    )
    color = models.CharField(
        max_length=20,
        verbose_name=_('color'),
    )
