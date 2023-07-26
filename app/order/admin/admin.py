"""
Storage admin
"""
###
# Libraries
###
from django.contrib import admin
from app.storage.models.storage import Storage


###
# Inline Admin Models
###

###
# Main Admin Models
###


class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'amount',)


admin.site.register(Storage, StorageAdmin)
