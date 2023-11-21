from django.contrib import admin

from .models import CartItem, Order, OrderItem, Product

admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
