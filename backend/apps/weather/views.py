from django.shortcuts import render
from backend.apps.weather import models
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from backend.apps.weather.serializers import WeatherSerializer, WeatherSerializerCreate, OpenWeatherSerializerCreate, WeatherSerializerRetrieve
from rest_framework.response import Response
from rest_framework import status
from backend.apps.additional_fields.models import TranslationField
from rest_framework import filters


class WeatherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = models.Weather.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name__ru', 'name__kk', 'name__en']

    def get_serializer_class(self):
        if self.action == "create":
            return WeatherSerializerCreate
        elif self.action == "retrieve":
            return WeatherSerializerRetrieve
        return WeatherSerializer

    def filter_queryset(self, queryset):
        is_deleted = self.request.query_params.get('is_deleted')
        if is_deleted == 'true':
            return queryset.filter(is_deleted=True)
        elif is_deleted == 'false':
            return queryset.filter(is_deleted=False)
        return queryset.filter()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        name = request.data.pop('name')
        coordinates = request.data.pop('coordinates')
        if serializer.is_valid(raise_exception=True):
            name_instance = TranslationField.objects.create(
                ru=name.get('ru'),
                kk=name.get('kk'),
                en=name.get('en')
            )
            coordinates_instance = models.Coordinates.objects.create(
                longitude=coordinates.get('longitude'),
                latitude=coordinates.get('latitude')
            )
            serializer.save(user_id=request.user, name=name_instance, coordinates=coordinates_instance)
            headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(serializer.data, 'fata')
        return Response(serializer.data)


class OpenWeatherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = models.OpenWeather.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return OpenWeatherSerializerCreate

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



