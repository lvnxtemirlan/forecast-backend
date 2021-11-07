from django.contrib import admin
from backend.apps.signup import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active']
    search_fields = ['username', 'first_name', 'email']


@admin.register(models.Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['key', 'user', 'created']
    # search_fields = ['username', 'first_name', 'email']