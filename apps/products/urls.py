from django.urls import path
from apps.products.views import *
from apps.products.api_endpoints.products.ProductList.views import *


urlpatterns = [
    path('products/', product_list, name='products'),
    path('categories/', category, name='categories'),
    path('category/<int:category_id>/', category_products, name='category_products'),
]