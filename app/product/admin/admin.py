"""
Product admin
"""
###
# Libraries
###
from django.contrib import admin
from app.product.models.product import Product


###
# Inline Admin Models
###


###
# Main Admin Models
###
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',
                    'description_short', 'description_long',
                    'image', 'size', 'brand',
                    'discount_price', 'is_active',
                    )


admin.site.register(Product, ProductAdmin)
