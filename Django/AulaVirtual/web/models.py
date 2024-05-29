from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI", unique=True)


# Crear Migracion
# python manage.py makemigrations web

# Ejecutar migracion