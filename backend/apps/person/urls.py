from django.urls import include, path
from backend.apps.person import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'person', views.PersonViewSet, basename='person')

urlpatterns = router.urls
