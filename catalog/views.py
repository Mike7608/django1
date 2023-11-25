from django.shortcuts import render

from catalog.models import Product


def product(request):
    id_item = request.GET["id"]
    prod = Product.objects.filter(id=id_item)
    context = {
        'objects_list': prod
    }
    return render(request, 'main/product.html', context)


def contacts(request):
    if request.method == 'post':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name}, {email}: {message}")
    return render(request, 'main/contacts.html')


def catalog(request):
    product_list = Product.objects.all()
    context = {
        'objects_list': product_list
    }
    return render(request,'main/catalog.html', context)
