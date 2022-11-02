from django.shortcuts import render
from appcoder.models import Curso
from django.http import HttpResponse
# Create your views here.

def listado_cursos(request):
    
    cursos = Curso.objects.all()

    cadena_respuesta= ''

    for curso in cursos:
        cadena_respuesta += curso.nombre + ' | '
    
    return HttpResponse(cadena_respuesta)