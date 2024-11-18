from rest_framework import generics

from shop_products.serializers import ProductSerializer
from shop_products.models import Product


class ProductCreateAPIView(generics.CreateAPIView):
    """ Класс создания продукта"""

    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    """ Класс просмотра списка продуктов"""

    serializer_class = ProductSerializer


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """ Класс просмотра продукта"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(generics.UpdateAPIView):
    """ Класс изменения продукта"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(generics.DestroyAPIView):
    """ Класс удаления продукта"""

    queryset = Product.objects.all()

