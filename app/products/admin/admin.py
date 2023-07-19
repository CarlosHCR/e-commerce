"""
Products admin
"""
###
# Libraries
###
from django.contrib import admin
from app.products.models.products import Product


###
# Inline Admin Models
###


###
# Main Admin Models
###
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description',
                    'image', 'size', 'brand',)


admin.site.register(Product, ProductAdmin)
