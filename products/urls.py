from django.urls import path

from products.views import index, products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
]
