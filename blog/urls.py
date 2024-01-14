from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, publish, BlogUpdateView, BlogDeleteView, is_creator

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>', publish, name='publish'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('<int:pk>', is_creator, name='is_creator')
]
