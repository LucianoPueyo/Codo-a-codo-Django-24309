from django.shortcuts import render
from rest_framework import viewsets
from web.models import Alumno
from .serializers import AlumnoSerializer
from rest_framework import permissions

class AlumnosViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]