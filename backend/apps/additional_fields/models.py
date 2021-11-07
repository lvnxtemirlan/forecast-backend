from django.db import models
from django.utils import timezone


class TranslationField(models.Model):
    class Meta:
        verbose_name = 'Поле с переводом'
        verbose_name_plural = 'Поля с переводом'

    ru = models.CharField(
        verbose_name='На русском',
        max_length=1000,
        default='',
        db_index=True
    )
    kk = models.CharField(
        verbose_name='На казахском',
        max_length=1000,
        default='',
        db_index=True,
        blank=True
    )
    en = models.CharField(
        verbose_name='На английском',
        max_length=1000,
        default='',
        db_index=True,
        blank=True
    )

    def __str__(self):
        try:
            if self:
                if self.ru:
                    return self.ru
                if self.kk:
                    return self.kk
                if self.en:
                    return self.en
            return 'Нет наименования'
        except:
            return 'Нет наименования'


class DictFields(models.Model):
    """
    Общие филды для справочников
    """

    class Meta:
        abstract = True

    name = models.ForeignKey(
        to='additional_fields.TranslationField',
        verbose_name='Наименование',
        on_delete=models.DO_NOTHING
    )
    code = models.CharField(
        verbose_name='Код для внутреннего использования',
        max_length=200,
        db_index=True,
        null=True, blank=True
    )
    is_default = models.BooleanField(
        default=False,
        verbose_name='Значение по умолчанию'
    )
    sort_number = models.PositiveIntegerField(
        verbose_name='Порядковое значение для сортировки',
        null=True, blank=True
    )


class CommonModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False)



