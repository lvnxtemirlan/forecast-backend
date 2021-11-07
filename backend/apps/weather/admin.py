from django.contrib import admin
from backend.apps.weather import models


@admin.register(models.Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'name', 'coordinates', 'is_deleted']
    search_fields = ['name__ru', 'name__kk', 'name_en']
    raw_id_fields = ['name', 'coordinates']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(models.Coordinates)
class CoordintesAdmin(admin.ModelAdmin):
    list_display = ['id', 'longitude', 'latitude']


@admin.register(models.OpenWeather)
class OpenWeatherAdmin(admin.ModelAdmin):
    list_display = ['id', 'weather_id', 'source', 'body']