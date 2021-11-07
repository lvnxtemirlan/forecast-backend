# from django.db.transaction import atomic
from rest_framework.serializers import ModelSerializer
from backend.apps.dictionary import models
from backend.apps.additional_fields import serializers
#
# class DictSerializer(ModelSerializer):
#     name = TranslationFieldSerializer(required=True)
#
#     def create(self, validated_data):
#         with atomic():
#             name = validated_data.pop('name', {})
#             validated_data['name'] = TranslationField.objects.create(**name)
#             return super().create(validated_data)
#
#     def update(self, instance, validated_data):
#         with atomic():
#             name = validated_data.pop('name', {})
#
#             if name:
#                 translation = TranslationField.objects.get(id=instance.name_id)
#                 for key, value in name.items():
#                     setattr(translation, key, value)
#                 translation.save()
#
#             return super().update(instance, validated_data)


class CitySerializer(ModelSerializer):
    name = serializers.TranslationFieldSerializer(required=True)

    class Meta:
        model = models.City
        fields = ['id', 'name', 'code', 'is_default']