from django.shortcuts import render

from .models import Product


def index(request):
    context = {"products": Product.objects.all()}
    return render(request, "shop/index.html", context)


def cart(request):
    return render(request, "shop/cart.html", {})


def orders(request):
    return render(request, "shop/orders.html", {})
