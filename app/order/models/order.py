###
# Libs
###
from django.db import models
from django.utils.translation import gettext as _
from app.storage.models.storage import Storage
from app.accounts.models.user import User
from app.payment.models.payment import Payment


###
# Model
###

class OrderItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    amount = models.IntegerField(
        verbose_name=_("Amount"),
        default=0,
    )


class Order(models.Model):
    ref_code = models.CharField(max_length=20)
    order_item = models.ManyToManyField(OrderItem, verbose_name=_("Order Item"))
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    payment = models.ForeignKey(
        Payment, on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
