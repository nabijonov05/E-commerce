from django.urls import path
from apps.products.views import *


urlpatterns = [
    path('products/', products, name='products'),
    path('categories/', category, name='categories'),
]