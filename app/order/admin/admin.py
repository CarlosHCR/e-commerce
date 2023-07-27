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
    list_display = ('id', 'storage', 'amount',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'ref_code', 'user', 'order_item', 'start_date',
                    'ordered_date', 'received',)


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
