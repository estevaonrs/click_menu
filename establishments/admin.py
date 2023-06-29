from django.contrib import admin

from . import models


class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ['establishments_category']


admin.site.register(models.Establishment,
                    EstablishmentAdmin, )
