from django.urls import path

from products.views import about_view, create_view, detail_view

urlpatterns = [
    path('about/', about_view, name='about'),
    path('create/', create_view, name='create'),
    path('<int:id>/', detail_view, name='detail')
]
