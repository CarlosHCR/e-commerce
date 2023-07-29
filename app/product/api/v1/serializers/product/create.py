"""
API V1: Products Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from app.product.models.product import Product
from app.product.models.size import Size
from app.product.models.color import Color


###
# Serializers
###


class CreateProductSerializer(serializers.ModelSerializer):
    size_name = serializers.CharField(write_only=True)
    color_name = serializers.CharField(write_only=True)

    def validate(self, attrs):
        size_name = attrs.pop('size_name')
        color_name = attrs.pop('color_name')
        try:
            size = Size.objects.get(size=size_name)
        except Size.DoesNotExist:
            size = Size.objects.create(size=size_name)
        try:
            color = Color.objects.get(color=color_name)
        except Color.DoesNotExist:
            color = Color.objects.create(color=color_name)
        attrs['size'] = size
        attrs['color'] = color
        return super().validate(attrs)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price',
                  'description_short', 'description_long',
                  'image', 'brand',
                  'discount_price', 'is_active', 'color_name', 'size_name',
                  )
