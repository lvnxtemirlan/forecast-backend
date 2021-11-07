from django.db import models


class Person(models.Model):
    class Meta:
        verbose_name_plural = "Пользовательи"
        verbose_name = "Пользователь"

    user_id = models.BigIntegerField(
        verbose_name='Основной пользователь',
        unique=True,
        db_index=True,
        null=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    middle_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )





