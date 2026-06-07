from django.shortcuts import render
from apps.products.models import *
from django.db.models import Count

# Create your views here.
def products(request):

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/product.html', context)

#=========================================================================================

def category(request):

    categories = Category.objects.annotate(product_count=Count('product'))

    context = {
        'categories': categories
    }

    return render(request, 'products/category.html', context)
