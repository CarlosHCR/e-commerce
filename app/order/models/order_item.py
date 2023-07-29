###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _
from app.product.models.product import Product


###
# Model
###

class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("Product"),
    )
    amount = models.IntegerField(
        default=0,
        verbose_name=_("Amount"),
    )
