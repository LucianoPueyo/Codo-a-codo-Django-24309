from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def saludar(request, nombre):
    print(request.method)

    return HttpResponse(f"<h1>Bienvenid@ {nombre}</h1>")

def alumnos_por_año(request, year):
    alumnos = ["Carlos", "Maria", "Jose"] # """"Levanta""""" los usuarios de la BBDD
    return HttpResponse(f"listado de alumnos: {year} \n {alumnos}")