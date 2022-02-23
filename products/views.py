from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    product = Product.objects.all()
    context = {'title': 'GeekShop - Продукты', 'products': product}

    return render(request, 'products/products.html', context)
