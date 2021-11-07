from django.contrib import admin
from . import models


@admin.register(models.TranslationField)
class TranslationFieldAdmin(admin.ModelAdmin):
    search_fields = ('ru', 'kk', 'en')
    list_display = ('id', 'ru', 'kk', 'en')
