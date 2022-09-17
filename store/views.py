from django.shortcuts import render, get_object_or_404
from .models import Product
from categories.models import Categories
# Create your views here.

def store(request, slug_id=None):
    category = None
    products = None
    if slug_id != None:
        category = get_object_or_404(Categories, slug=slug_id)
        products = Product.objects.filter(is_available=True, category=category)
    else:
        products = Product.objects.all().filter(is_available=True)

    dictionary = {
        'products': products
    }
    return render(request, 'store/store.html', dictionary)

def product_details(request, slug_id, product_slug):
    try:
        product_in_detail = Product.objects.get(category__slug=slug_id, slug=product_slug)
    except:
        raise Exception

    context = {
        'product': product_in_detail,
    }
    return render(request, 'store/product_detail.html', context)
