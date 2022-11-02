from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def vista_saludo(request):
    return HttpResponse("Hola coders! :) ")

def dia_hoy(request,nombre):
    hoy = datetime.now()
    respuesta = f"Hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)

def anio_nacimiento(request,edad):
    anio = datetime.now().year - int(edad)
    respuesta = f"Tenes {edad} anios asi que naciste en el {anio}"
    return HttpResponse(respuesta)

def vista_plantilla(request):
    #abrimos el archivo
    archivo = open('C:/Users/matil/Desktop/Mati/Coderhouse/17_DJANGO/bottiglia/bottiglia/templates/plantilla_bonita.html')
    
    #creamos el objeto plantilla
    plantilla = Template(archivo.read())
    
    #cerramos el archivo para liberar recursos
    archivo.close()
    
    #diccionario con datos para la plantilla
    datos ={'nombre':'Matias', 'fecha':datetime.now(), 'apellido':'Salinas'}
    

    #creamos el contexto
    contexto = Context(datos)

    #renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def vista_listado_alumnos(request):

    #abrimos el archivo
    archivo = open(r'C:\Users\matil\Desktop\Mati\Coderhouse\17_DJANGO\bottiglia\bottiglia\templates\listado_alumnos.html')

    #creamos el template
    plantilla = Template(archivo.read())

    #cerramos el archivo
    archivo.close()

    #creamos el diccionario de datos
    listado_alumnos = ['Leonel Gareis','Cristian Russo', 'Jorge Garcia','Diego Ibarra', 'Matias Salinas','Santiago Ortiz','Barbara Vivante']

    datos = {'tecnologia':'Python', 'listado_alumnos':listado_alumnos}

    #creamos el contexto
    contexto = Context(datos)

    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def vista_listado_alumnos2(request):

    listado_alumnos = ['Leonel Gareis','Cristian Russo', 'Jorge Garcia','Diego Ibarra', 'Matias Salinas','Santiago Ortiz','Barbara Vivante']

    datos = {'tecnologia':'Python', 'listado_alumnos':listado_alumnos}

    plantilla = loader.get_template('listado_alumnos.html')
    documento = plantilla.render(datos)

    return HttpResponse(documento)