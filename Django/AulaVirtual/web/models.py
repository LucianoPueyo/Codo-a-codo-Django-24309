from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from AulaVirtual import settings


class Persona(models.Model):
    dni = models.IntegerField(verbose_name="DNI", unique=True)

    class Meta:
        abstract = True


class Alumno(Persona):
    """
        https://stackoverflow.com/questions/71423191/django-user-model-with-same-fields
    """
    LE = models.IntegerField(verbose_name="Libreta Estudiantil", unique=True, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}| DNI:{self.dni} | LE: {self.LE}"


class Docente(Persona):
    CUIT = models.IntegerField(verbose_name="CUIT", unique=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | DNI:{self.dni} | CUIT: {self.CUIT}"

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
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True, blank=True)
    alumnos = models.ManyToManyField(Alumno, through='Inscripcion')

    def __str__(self):
        return f"{self.nombre} | {self.turno} | Docente: {self.docente.nombre_completo() if self.docente else '---'}"

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(verbose_name="Fecha de inscripción", auto_now_add=True)
