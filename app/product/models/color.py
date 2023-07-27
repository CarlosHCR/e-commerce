###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _


###
# Model
###


class Color(models.Model):
    color = models.CharField(
        max_length=30,
        verbose_name=_('color'),
    )
