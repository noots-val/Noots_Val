from portfolio.models import Commodity
from portfolio.models import User
from portfolio.models import Cart
from django.contrib import admin


class CommodityAdmin(admin.ModelAdmin):
    list_display = ("id", "commodity_title", "category", "stock")
    search_fields = ["commodity_title"]
    ordering = ("id",)


class UserAdmin(admin.ModelAdmin):
    list_display = ("id",)
    ordering = ("id",)


class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "commodity", "amount")
    ordering = ("id",)


admin.site.register(Commodity, CommodityAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Cart, CartAdmin)
