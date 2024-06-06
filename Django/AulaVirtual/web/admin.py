from django.contrib import admin
from .models import Alumno, Docente, Curso, Inscripcion

admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Inscripcion)