from rest_framework.serializers import ModelSerializer
from backend.apps.additional_fields.serializers import TranslationFieldSerializer
from backend.apps.weather.models import Weather, Coordinates, OpenWeather
from rest_framework import serializers


class CoordinatesSerializer(ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('longitude', 'latitude')


class OpenWeatherSerializer(ModelSerializer):
    class Meta:
        model = OpenWeather
        fields = ('weather', 'body', 'created_at', 'updated_at')


class WeatherSerializer(ModelSerializer):
    name = TranslationFieldSerializer(required=True)
    coordinates = CoordinatesSerializer(read_only=True)

    class Meta:
        model = Weather
        fields = ('id', 'name', 'coordinates', 'is_deleted')


class WeatherSerializerRetrieve(ModelSerializer):
    name = TranslationFieldSerializer(required=True)
    weathers = OpenWeatherSerializer(read_only=True, many=True)

    class Meta:
        model = Weather
        fields = ('name', 'weathers')


class WeatherSerializerCreate(ModelSerializer):
    name = TranslationFieldSerializer(read_only=True)
    coordinates = CoordinatesSerializer(read_only=True)

    class Meta:
        model = Weather
        fields = ('name', 'coordinates')


class OpenWeatherSerializerCreate(ModelSerializer):
    class Meta:
        model = OpenWeather
        fields = ('weather', 'body')




