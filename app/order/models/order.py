###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _
from app.accounts.models.user import User
from app.address.models.address import Address
from app.order.models.order_item import OrderItem


###
# Model
###


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("User")
    )
    delivery_address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name=_("Delivery Address")
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
    delivery_date = models.DateField(
        verbose_name=_("Ordered Date")
    )
    received = models.BooleanField(
        default=False,
        verbose_name=_("Received")
    )
