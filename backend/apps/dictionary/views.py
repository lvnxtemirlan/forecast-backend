from backend.apps.dictionary import models
from rest_framework import viewsets
from backend.apps.additional_fields.serializers import TranslationFieldSerializer
from backend.apps.dictionary.serializers import CitySerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name__ru', 'name__kk', 'name__en', 'code']

