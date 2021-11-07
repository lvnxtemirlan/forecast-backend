from django.urls import include, path
from backend.apps.dictionary import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'city', views.CityViewSet, basename='city')

urlpatterns = router.urls
