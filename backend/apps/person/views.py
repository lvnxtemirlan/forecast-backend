from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import models
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Person.objects.all()
    serializer_class = PersonSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name__ru', 'name__kk', 'name__en', 'code']



