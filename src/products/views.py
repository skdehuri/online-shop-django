from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from products.forms import ProductForm
from products.models import Product
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!</h1>")
    product_objects = Product.objects.all()
    context = {
        'products': product_objects
    }
    return render(request, 'home.html', context)


def about_view(request, *args, **kwargs):
    context = {
        'test': 'my context',
        'list_item': [123, 345, 567, 789]
    }
    return render(request, 'about.html', context)


def detail_view(request, id, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!</h1>")
    product_objects = get_object_or_404(Product, id=id)
    context = {
        'product': product_objects
    }
    return render(request, 'detail.html', context)


