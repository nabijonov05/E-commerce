from django.shortcuts import render
from apps.products.models import *
from django.db.models import Count
from django.shortcuts import render, get_object_or_404

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

#=========================================================================================

def category_products(request, category_id):
  
    category = get_object_or_404(Category, id=category_id)
    
    products = Product.objects.filter(category=category)
    

    context = {
        'category': category,
        'products': products
    }
    return render(request, 'products/product.html', context)
