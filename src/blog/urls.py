from django.urls import path

from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('create', ArticleCreateView.as_view(), name='create'),
]
