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

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        unique=True,
        verbose_name=_("Product"),
        error_messages={
            "unique": _("This product already exists in storage.")
        }
    )
    amount = models.IntegerField(
        verbose_name=_("Amount"),
        default=0
    )
