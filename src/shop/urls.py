from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.cart, name="cart"),
    path("orders/", views.orders, name="orders"),
    path("add/", views.add_product_to_cart, name="add"),
    path("checkout/", views.checkout, name="checkout"),
    path("product/<int:id>/", views.product, name="product"),
]
