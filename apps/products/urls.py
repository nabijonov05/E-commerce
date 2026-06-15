from django.urls import path
from apps.products.views import *
from apps.products.api_endpoints.products.ProductList.views import ProductListAPIView
from apps.products.api_endpoints.products.ProductCreate.views import ProductCreateAPIView
from apps.products.api_endpoints.products.ProductDetail.views import ProductDetailAPIView
from apps.products.api_endpoints.products.ProductUpdateDestroy.views import ProductUpdateAPIView, ProductDestroyAPIView
from apps.products.api_endpoints.categories.CategoryList.views import CategorListAPIView
from apps.products.api_endpoints.categories.CategoryDetail.views import CategorDetailAPIView
from apps.products.api_endpoints.categories.CategoryCreate.views import CategorCreateAPIView
from apps.products.api_endpoints.categories.CategoryUpdateDestroy.views import CategorUpdateAPIView, CategorDestroyAPIView


urlpatterns = [
    path('', ProductListAPIView.as_view(), name='products'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view(), name='product_delete'),

    path('categories/', CategorListAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategorDetailAPIView.as_view(), name='category_detail'),
    path('categories/create/', CategorCreateAPIView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategorUpdateAPIView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategorDestroyAPIView.as_view(), name='category_delete'),
]