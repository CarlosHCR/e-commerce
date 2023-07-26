###
# Libs
###
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from app.address.models.address import Address


###
# Model
###


class User(AbstractUser):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
