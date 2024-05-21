from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from .forms import *

import datetime

def index(request):
    # Accedo a la BBDD a traves de los modelos

    contexto = {
        'name': 'Maria',
        'fecha_hora': datetime.datetime.now()
    }

    return render(request, 'web/index.html', contexto)

def saludar(request, nombre):
    print(request.method)

    return HttpResponse(f"<h1>Bienvenid@ {nombre}</h1>")

def alumnos_por_año(request, year):
    alumnos = ["Carlos", "Maria", "Jose"] # """"Levanta""""" los usuarios de la BBDD
    return HttpResponse(f"listado de alumnos: {year} \n {alumnos}")

def listado_alumnos(request):

    contexto = {
        'alumnos': [
            'Carlos Lopez',
            'Maria Del Cerro',
            'Gaston Perez'
        ],

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
            
            messages.success(request, 'El alumno fue dado de alta con éxito')

            return redirect('index')

        # Si el form es incorrecto
        # Se renderiza un form con mensajes de error  

    return render(request, 'web/alta_alumno.html', contexto)
