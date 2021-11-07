from django.urls import include, path
from rest_framework import routers

from backend.apps.weather import views


urlpatterns = [
    path('', views.WeatherViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/', views.WeatherViewSet.as_view({
        'put': 'partial_update',
        'get': 'retrieve',
    })),
    path('generate_weather/', views.OpenWeatherViewSet.as_view({
        'post': 'create'
    }))

]