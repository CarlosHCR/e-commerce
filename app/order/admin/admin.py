"""
Storage admin
"""
###
# Libraries
###
from django.contrib import admin
from app.order.models.order import Order
from app.order.models.order_item import OrderItem


###
# Inline Admin Models
###

###
# Main Admin Models
###

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'amount',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'delivery_address', 'order_item', 'start_date',
                    'delivery_date', 'received',)


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
