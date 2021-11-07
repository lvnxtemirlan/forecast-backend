from rest_framework.serializers import ModelSerializer
from backend.apps.additional_fields import models


class TranslationFieldSerializer(ModelSerializer):
    """Для получения поля с переводом"""

    class Meta:
        model = models.TranslationField
        fields = ('ru', 'kk', 'en')