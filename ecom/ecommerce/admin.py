from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'price', 'category',
        'sale', 'published', 'created'
    ]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(DailyOffer)
