###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _
from app.product.models.size import Size
from app.product.models.color import Color


###
# Model
###


class Product(models.Model):

    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name=_('Name'),
        error_messages={
            "unique": _("This product already exists in storage.")
        }
    )
    price = models.FloatField(verbose_name=_('price'))
    description_short = models.TextField(verbose_name=_('Description short'))
    description_long = models.TextField(verbose_name=_('Description long'))
    image = models.ImageField(
        upload_to='products',
        verbose_name=_('image'),
    )
    brand = models.CharField(
        max_length=20,
        verbose_name=_('Brand'),
    )
    discount_price = models.FloatField(
        blank=True,
        null=True,
        verbose_name=_('Discount price')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is active')
    )
    size = models.ForeignKey(
        Size,
        verbose_name=_('Size'),
        on_delete=models.CASCADE
    )
    color = models.ForeignKey(
        Color,
        verbose_name=_("Color"),
        on_delete=models.CASCADE
    )
