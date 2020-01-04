from django.http import HttpResponse
from django.shortcuts import render

from products.models import Product


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!</h1>")
    product_object = Product.objects.get(id=1)
    context = {
        'title': product_object.title,
        'price': product_object.price
    }
    return render(request, 'home.html', context)


def about_view(request, *args, **kwargs):
    context = {
        'test': 'my context',
        'list_item': [123, 345, 567, 789]
    }
    return render(request, 'about.html', context)
