from django.shortcuts import render
from django.http import HttpResponse
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