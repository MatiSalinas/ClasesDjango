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
    return render(request,'appcoder/cursos.html')

def estudiantes(request):
    return render(request,'appcoder/estudiantes.html')

def profesores(request):
    return render(request,'appcoder/profesores.html')

def entregables(request):
    return render(request,'appcoder/entregables.html')