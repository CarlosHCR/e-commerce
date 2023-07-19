###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _


###
# Model
###


class Product(models.Model):

    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name=_('name'),
        error_messages={
            "unique": _("This product already exists in storage.")
        }
    )
    price = models.FloatField(
        verbose_name=_('price'),
    )
    description_short = models.TextField(
        verbose_name=_('description short'),
    )
    description_long = models.TextField(
        verbose_name=_('description long'),
    )
    image = models.ImageField(
        upload_to='products',
        verbose_name=_('image'),
    )
    size = models.CharField(
        max_length=10,
        verbose_name=_('size'),
    )
    brand = models.CharField(
        max_length=20,
        verbose_name=_('brand'),
    )
    discount_price = models.FloatField(
        blank=True,
        null=True,
        verbose_name=_('discount price')
    )
    is_active = models.BooleanField(default=True)
