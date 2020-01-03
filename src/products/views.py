from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!</h1>")
    context = {
        'test': 'my context'
    }
    return render(request, 'home.html', context)


def about_view(request, *args, **kwargs):
    context = {
        'test': 'my context'
    }
    return render(request, 'about.html', context)
