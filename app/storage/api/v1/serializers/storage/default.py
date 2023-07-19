"""
API V1: Storage Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from app.storage.models.storage import Storage

###
# Serializers
###


class DefaultStorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = '__all__'
