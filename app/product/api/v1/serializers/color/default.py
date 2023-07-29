"""
API V1: Color Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from app.product.models.color import Color

###
# Serializers
###


class DefaultColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'
