"""
API V1: OrderItem Serializers
"""
###
# Libraries
###
from rest_framework import serializers, exceptions
from app.order.models.order_item import OrderItem
from app.storage.models.storage import Storage

###
# Serializers
###


class CreateOrderItemSerializer(serializers.ModelSerializer):
    storage = serializers.IntegerField(write_only=True)


    def validate(self, attrs):
        storage_id = attrs.get('storage')
        amount = attrs.get('amount')
        try:
            storage = Storage.objects.get(id=storage_id)
        except Storage.DoesNotExist:
            raise exceptions.ValidationError('Storage not found.')
        if storage.amount < amount:
            raise exceptions.ValidationError(
                'The quantity in the order item cannot be greater than the quantity in storage.')
        else:
            storage.amount -= amount
            storage.save()
        attrs['storage'] = storage
        return super().validate(attrs)


    class Meta:
        model = OrderItem
        fields = '__all__'
