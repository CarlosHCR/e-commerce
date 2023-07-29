###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _
from app.accounts.models.user import User

###
# Model
###


class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )
    street = models.CharField(
        max_length=512,
        verbose_name=_('Street/Avenue'),
    )
    number = models.CharField(
        max_length=16,
        verbose_name=_('Number'),
    )
    extra = models.CharField(
        max_length=64,
        verbose_name=_('Extra'),
    )
    neighborhood = models.CharField(
        max_length=64,
        verbose_name=_('Neighborhood'),
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
        verbose_name=_('Zip code'),
    )
