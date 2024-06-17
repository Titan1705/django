from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"products": product}
    return render(request, 'products_detail.html', context)