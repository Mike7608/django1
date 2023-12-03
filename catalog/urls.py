from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, contacts, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductsListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_view')
]