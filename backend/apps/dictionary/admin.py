from django.contrib import admin
from . import models as dictionary


@admin.register(dictionary.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    search_fields = ("name__ru", "name__kk", "name_en")
