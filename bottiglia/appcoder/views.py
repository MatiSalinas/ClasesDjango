from django.shortcuts import render
from appcoder.models import Curso
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def listado_cursos(request):
    
    cursos = Curso.objects.all()

    cadena_respuesta= ''

    for curso in cursos:
        cadena_respuesta += curso.nombre + ' | '
    
    return HttpResponse(cadena_respuesta)

def inicio(request):
    return render(request, 'appcoder/index.html')

def cursos(request):
    return HttpResponse('Estas en cursos')

def estudiantes(request):
    return HttpResponse('Estas en estudiantes')

def profesores(request):
    return HttpResponse('Estas en profesores')

def entregables(request):
    return HttpResponse('Estas en entregables')