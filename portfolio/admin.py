from portfolio.models import Product
from portfolio.models import Cart
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product_title", "category", "stock")
    search_fields = ["product_title"]
    ordering = ("id",)

class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "amount")
    ordering = ("id",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
