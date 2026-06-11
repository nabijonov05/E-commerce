from django.urls import path
from apps.products.views import *
from apps.products.api_endpoints.products.ProductList.views import *
from apps.products.api_endpoints.products.ProductCreate.views import product_create_view
from apps.products.api_endpoints.products.ProductDetail.views import product_detail_view
from apps.products.api_endpoints.products.ProductUpdateDestroy.views import product_update_destroy_view

urlpatterns = [
    path('products/', product_list, name='products'),
    path('categories/', category, name='categories'),
    path('category/<int:category_id>/', category_products, name='category_products'),
    path('create/', product_create_view, name='order-create'),
    path('<int:pk>/', product_detail_view, name='order-detail'),
    path('<int:pk>/update/', product_update_destroy_view, name='order-update'),
    path('<int:pk>/delete/', product_update_destroy_view, name='order-delete'),
]