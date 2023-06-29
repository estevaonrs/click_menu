from django.contrib import admin

from . import models


class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_item', 'item_name',
                    'category', 'value', 'item_description']


class MenuNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.MenuName, MenuNameAdmin)
