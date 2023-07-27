"""
Product admin
"""
###
# Libraries
###
from django.contrib import admin
from app.product.models.product import Product
from app.product.models.size import Size
from app.product.models.color import Color


###
# Inline Admin Models
###


###
# Main Admin Models
###
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',
                    'description_short', 'description_long',
                    'image', 'brand',
                    'discount_price', 'is_active', 'color', 'size',
                    )


class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color',)


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
