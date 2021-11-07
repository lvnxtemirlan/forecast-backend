from rest_framework.serializers import ModelSerializer
from . import models

class PersonSerializer(ModelSerializer):
    class Meta:
        models = models.Person
        fields = ("__all__")