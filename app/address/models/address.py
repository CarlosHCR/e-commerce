###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _


###
# Model
###


class Address(models.Model):
    street = models.CharField(
        max_length=512,
        verbose_name=_('street/avenue'),
    )
    number = models.CharField(
        max_length=16,
        verbose_name=_('number'),
    )
    extra = models.CharField(
        max_length=64,
        verbose_name=_('extra'),
    )
    neighborhood = models.CharField(
        max_length=64,
        verbose_name=_('neighborhood'),
    )
    city = models.CharField(
        max_length=256,
        verbose_name=_('City'),
    )
    state = models.CharField(
        max_length=2,
        verbose_name=_('State'),
    )
    zip_code = models.CharField(
        max_length=8,
        verbose_name=_('zip code'),
    )
