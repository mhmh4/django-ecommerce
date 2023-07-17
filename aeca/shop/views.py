from django.shortcuts import render

from .models import Product


def index(request):
    context = {"products": Product.objects.all()}
    return render(request, "shop/index.html", context)
