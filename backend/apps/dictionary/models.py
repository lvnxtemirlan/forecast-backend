from django.db import models
from backend.apps.additional_fields.models import DictFields


class City(DictFields):

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    coordinates = models.ForeignKey(
        to='weather.Coordinates',
        verbose_name='Координаты',
        on_delete=models.DO_NOTHING,
        null=True,
        related_name='coordinatess'
    )


