from django.shortcuts import render, redirect

from .models import CartItem, Order, OrderItem, Product


def index(request):
    context = {
        "products": Product.objects.all(),
        "cart": CartItem.objects.filter(user=request.user.id)
    }
    return render(request, "shop/index.html", context)


def product(request, id):
    product = Product.objects.filter(id=id).get()
    context = {
        "product": product
    }
    return render(request, "shop/product.html", context)


def add_product_to_cart(request):
    product_id = request.POST.get("product_id")
    product = Product.objects.filter(id=product_id).get()
    if CartItem.objects.filter(user=request.user, product=product).exists():
        return redirect("index")
    item = CartItem(user=request.user, product=product)
    item.save()
    return redirect("index")


def cart(request):
    context = {
        "cart": CartItem.objects.filter(user=request.user.id)
    }
    cart_total = sum(item.product.price for item in context["cart"])
    context["cart_total"] = cart_total
    return render(request, "shop/cart.html", context)


def checkout(request):
    order = Order(user=request.user)
    order.save()
    # order.id should be usuable
    cart = CartItem.objects.filter(user=request.user)
    for item in cart:
        oi = OrderItem(order=order, product=item.product)
        oi.save()
        item.delete()
    return render(request, "shop/cart.html", {})


def orders(request):
    context = {
        "orders": Order.objects.filter(user=request.user)
    }
    return render(request, "shop/orders.html", context)
