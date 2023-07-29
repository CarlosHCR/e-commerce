"""
Address admin
"""
###
# Libraries
###
from django.contrib import admin
from app.address.models.address import Address

###
# Inline Admin Models
###

###
# Main Admin Models
###


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'street', 'number', 'extra',
                    'neighborhood', 'city', 'state', 'zip_code',)


admin.site.register(Address, AddressAdmin)
