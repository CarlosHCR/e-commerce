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
        unique=True,
        verbose_name=_('Color'),
        error_messages={"unique": "This color already exists"}
    )
