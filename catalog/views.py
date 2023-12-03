from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = "main/product.html"


def contacts(request):
    if request.method == 'post':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name}, {email}: {message}")
    return render(request, 'main/contacts.html')


class ProductsListView(ListView):
    model = Product
    template_name = "main/product_list.html"
