from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Alumno(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI", unique=True)


class Docente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.IntegerField(verbose_name="DNI", unique=True)
    CUIT = models.IntegerField(verbose_name="CUIT", unique=True)


class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    turno = models.CharField(max_length=50, verbose_name="Turno")
    cupos = models.IntegerField(verbose_name="Cupos",
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]   
    )
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de finalización")
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True)
    alumnos = models.ManyToManyField(Alumno, through='Inscripcion')


class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(verbose_name="Fecha de inscripción", auto_now_add=True)
