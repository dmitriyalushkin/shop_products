from django.urls import path

from shop_products.apps import ShopProductsConfig
from shop_products.views_products import (ProductCreateAPIView,
                                          ProductListAPIView,
                                          ProductRetrieveAPIView,
                                          ProductUpdateAPIView,
                                          ProductDestroyAPIView)

app_name = ShopProductsConfig.name

urlpatterns = [
    path('product/create/', ProductCreateAPIView.as_view(),
         name='product-create'),
    path('product/', ProductListAPIView.as_view(),
         name='product-list'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(),
         name='product-get'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(),
         name='product-update'),
    path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(),
         name='product-delete'),
]
