from django.db import models
from backend.apps.additional_fields.models import TranslationField, CommonModel


class SourceTypeChoices(models.TextChoices):
    OPEN_WEATHER = "OPEN_WEATHER", "Open Weather data"
    OTHER = "OPEN_WEATHER_PREMIUM", "PREMIUM Open Weather data"


class Weather(CommonModel):
    class Meta:
        verbose_name_plural = "Погоды"
        verbose_name = "Погода"

    user_id = models.ForeignKey(to='signup.CustomUser',
                                verbose_name="Основной пользователь",
                                related_name='signup_user',
                                on_delete=models.CASCADE,
                                null=True, blank=True)

    name = models.ForeignKey(
        to='additional_fields.TranslationField',
        verbose_name='Наименование',
        on_delete=models.DO_NOTHING,
        null=True
    )

    coordinates = models.ForeignKey(
        to='weather.Coordinates',
        verbose_name='Координаты',
        on_delete=models.DO_NOTHING,
        null=True,
        related_name='coordinates'
    )


class OpenWeather(CommonModel):
    class Meta:
        verbose_name = "OpenWeather"
        verbose_name_plural = "OpenWeathers"

    weather = models.ForeignKey(
        to='weather.Weather',
        verbose_name="ID погоды",
        on_delete=models.DO_NOTHING,
        null=True,
        related_name='weathers'
    )

    source = models.CharField(
        choices=SourceTypeChoices.choices,
        default=SourceTypeChoices.OPEN_WEATHER,
        verbose_name="Вид погодных данных",
        max_length=30,
        null=True, blank=True
    )

    body = models.TextField(
        null=True, blank=True,
        verbose_name="Данные о погоде"
    )


class Coordinates(models.Model):
    class Meta:
        verbose_name_plural = "Координаты"
        verbose_name = "Координата"
    longitude = models.FloatField(verbose_name="Долгота",
                                  blank=True, null=True, )
    latitude = models.FloatField(verbose_name="Широта",
                                 blank=True, null=True, )

    def __str__(self):
        return "{}, {}".format(self.longitude, self.latitude)
