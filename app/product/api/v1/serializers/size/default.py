"""
API V1: Size Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from app.product.models.size import Size

###
# Serializers
###


class DefaultSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'
