from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, publish, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='view'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>', publish, name='publish'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
