"""
API V1: Order Serializers
"""
###
# Libraries
###
from rest_framework import serializers, exceptions
from app.order.models.order import Order
from app.order.models.order_item import OrderItem
from app.storage.models.storage import Storage

###
# Serializers
###


class CreateOrderSerializer(serializers.ModelSerializer):

    order_item = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        order_item_id = attrs.get('order_item')
        try:
            order_item = OrderItem.objects.get(id=order_item_id)
            storage = Storage.objects.get(product=order_item.product)
        except OrderItem.DoesNotExist:
            raise exceptions.ValidationError('Order item not found.')
        except Storage.DoesNotExist:
            raise exceptions.ValidationError('Storage not found.')
        if order_item.amount > storage.amount:
            raise exceptions.ValidationError(
                'The quantity in the order item cannot be greater than the quantity in storage.')
        storage.amount -= order_item.amount
        storage.save()
        attrs['order_item'] = order_item
        return attrs

    class Meta:
        model = Order
        fields = (
            'id',
            'order_item',
            'ref_code',
            'ordered_date',
        )
