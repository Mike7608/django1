from django.urls import path

from catalog.apps import MainConfig
from catalog.views import catalog, contacts, product

app_name = MainConfig.name

urlpatterns = [
    path('', catalog, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', product, name='product')
]