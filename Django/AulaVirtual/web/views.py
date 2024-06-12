from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import Alumno, Docente
import datetime

def index(request):
    # Accedo a la BBDD a traves de los modelos

    contexto = {
        'fecha_hora': datetime.datetime.now()
    }

    return render(request, 'web/index.html', contexto)

def user_logout(request):
    logout(request)

    messages.success(request, 'Sesion Cerrada')

    return redirect('index')

def saludar(request, nombre):
    print(request.method)

    return HttpResponse(f"<h1>Bienvenid@ {nombre}</h1>")

def alumnos_por_año(request, year):
    alumnos = ["Carlos", "Maria", "Jose"] # """"Levanta""""" los usuarios de la BBDD
    return HttpResponse(f"listado de alumnos: {year} \n {alumnos}")

@login_required
def listado_alumnos(request):
    alumnos = Alumno.objects.all().order_by('dni') # QuerySet

    contexto = {
        'alumnos': alumnos,
        'cuota_al_dia': True
    }

    return render(request, 'web/listado_alumnos.html', contexto)

def alta_alumno(request):
    contexto = {}

    if request.method == "GET":
        contexto['alta_alumno_form'] = AltaAlumnoForm()
    
    else: # Asumo que es un POST
        form = AltaAlumnoForm(request.POST)
        contexto['alta_alumno_form'] = form
        
        # Validar el form
        if form.is_valid():
            # Si el form es correcto
            # Lo redirijo a una vista segura por ejemplo el index
            
            nuevo_alumno = Alumno(
                nombre = form.cleaned_data['nombre'], 
                apellido = form.cleaned_data['apellido'], 
                dni = form.cleaned_data['dni'], 
                LE = form.cleaned_data['dni'] + 10000
            )

            nuevo_alumno.save()

            messages.success(request, 'El alumno fue dado de alta con éxito')

            return redirect('index')

        # Si el form es incorrecto
        # Se renderiza un form con mensajes de error  

    return render(request, 'web/alta_alumno.html', contexto)


class DocenteListView(LoginRequiredMixin, ListView):
    model=Docente
    context_object_name='docentes'
    template_name='web/listado_docentes.html'
    ordering = ['dni']


def alta_docente(request):
    contexto = {}

    if request.method == "GET":
        formulario = AltaDocenteModelForm()

    else:
        formulario = AltaDocenteModelForm(request.POST)

        if formulario.is_valid():
            formulario.save()

            messages.success(request, 'El docente fue dado de alta con éxito')
            return redirect('index')

    contexto["formulario"] = formulario
    return render(request, 'web/alta_docente.html', contexto)