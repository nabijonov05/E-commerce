from django.urls import path
from apps.products.views import *
from apps.products.api_endpoints.products.ProductList.views import product_list
from apps.products.api_endpoints.products.ProductCreate.views import product_create
from apps.products.api_endpoints.products.ProductDetail.views import product_detail
from apps.products.api_endpoints.products.ProductUpdateDestroy.views import product_update_destroy
from apps.products.api_endpoints.categories.CategoryList.views import category_list
from apps.products.api_endpoints.categories.CategoryDetail.views import category_detail
from apps.products.api_endpoints.categories.CategoryCreate.views import category_create
from apps.products.api_endpoints.categories.CategoryUpdateDestroy.views import category_update_destroy


urlpatterns = [
    path('', product_list, name='products'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('create/', product_create, name='product_create'),
    path('<int:pk>/update/', product_update_destroy, name='product_update'),
    path('<int:pk>/delete/', product_update_destroy, name='product_delete'),

    path('categories/', category_list, name='categories'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/<int:pk>/update/', category_update_destroy, name='category_update'),
    path('categories/<int:pk>/delete/', category_update_destroy, name='category_delete'),
]