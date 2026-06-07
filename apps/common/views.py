from django.shortcuts import render
from apps.products.models import *
from django.db.models import Count

def index(request):
    
    products = Product.objects.all()
    
    categories = Category.objects.annotate(product_count=Count('product'))
    
    context = {
        'products': products,
        'categories': categories 
    }

    return render(request, 'common/index.html', context)