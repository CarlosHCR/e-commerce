###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _
from app.accounts.models.user import User
from app.order.models.order_item import OrderItem


###
# Model
###


class Order(models.Model):
    ref_code = models.CharField(max_length=20, verbose_name=_("Ref Code"))
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("User")
    )
    order_item = models.ForeignKey(
        OrderItem,
        on_delete=models.CASCADE,
        verbose_name=_("Order Item")
    )
    start_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Start Date")
    )
    ordered_date = models.DateTimeField(
        verbose_name=_("Ordered Date")
    )
    received = models.BooleanField(
        default=False,
        verbose_name=_("Received")
    )
