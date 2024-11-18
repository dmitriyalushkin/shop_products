from rest_framework import serializers

from shop_products.models import Product


class ProductSerializer(serializers.Serializer):
    """ Сериализатор для модели продуктов"""

    class Meta:
        model = Product
        fields = '__all__'
