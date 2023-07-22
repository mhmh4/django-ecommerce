from django.shortcuts import render, redirect

from .models import CartItem, Product


def index(request):
    context = {
        "products": Product.objects.all(),
        "cart": CartItem.objects.filter(user=request.user.id)
    }
    return render(request, "shop/index.html", context)


def add_product_to_cart(request):
    product_id = request.POST["product_id"]
    product = Product.objects.filter(id=product_id).get()
    item = CartItem(user=request.user, product=product)
    item.save()
    return redirect("index")


def cart(request):
    context = {
        "cart": CartItem.objects.filter(user=request.user.id)
    }
    return render(request, "shop/cart.html", context)


def orders(request):
    return render(request, "shop/orders.html", {})
