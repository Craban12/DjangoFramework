from django.urls import path

from products.views import index, products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category<int:category_id>', products, name='category'),
    path('page/<int:page>/', products, name='page'),
]
