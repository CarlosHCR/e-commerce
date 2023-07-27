###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _


###
# Model
###


class Size(models.Model):

    size = models.CharField(
        max_length=5,
        unique=True,
        verbose_name=_('Size'),
        error_messages={
            "unique": _("This size already exists.")
        }
    )
