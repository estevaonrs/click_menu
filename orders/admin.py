from django.contrib import admin

from . import models


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['OrdersPhone', 'enable']


admin.site.register(models.Orders, OrdersAdmin)
