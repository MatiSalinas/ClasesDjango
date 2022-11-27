from django.shortcuts import render
from appcoder.models import *
from django.http import HttpResponse
from django.shortcuts import render,redirect
from appcoder.forms import ProfesorFormulario,CursoFormulario, userRegisterForm

from django.contrib.auth.mixins import LoginRequiredMixin

#class-based views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def listado_cursos(request):
    
    cursos = Curso.objects.all()

    cadena_respuesta= ''

    for curso in cursos:
        cadena_respuesta += curso.nombre + ' | '
    
    return HttpResponse(cadena_respuesta)

def inicio(request):
    return render(request, 'appcoder/index.html')

@login_required
def cursos(request):
    errores = ''
    #validamos el tipo de peticiones
    if request.method == 'POST':
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'],camada=data['camada'])
            curso.save()
        else:
            #si el formulario no es valido
            errores = formulario.errors
    #recuperar todos los cursos de la base de datos
    cursos = Curso.objects.all()
    #creamos el formulario vacio
    formulario = CursoFormulario()
    #creamos el contexto
    contexto = {'listado_cursos':cursos,'formulario':formulario,'errores':errores}
    #retornamos la repuesta
    return render(request,'appcoder/cursos.html',contexto)

def estudiantes(request):
    return render(request,'appcoder/estudiantes.html')

def profesores(request):
    return render(request,'appcoder/profesores.html')

def creacion_profesores(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)
        
        #validamos que el formulario o tenga problemas
        if formulario.is_valid():
            data = formulario.cleaned_data

            profesor = Profesor(nombre=data['nombre'],apellido=data['apellido'],email=data['email'],profesion=data['profesion'])
            profesor.save()
            formulario = ProfesorFormulario()
            return render(request, 'appcoder/crear_profesores.html',{'formulario':formulario})

    else:
        formulario = ProfesorFormulario()
    return render(request, 'appcoder/crear_profesores.html',{'formulario':formulario})

def buscar_curso(request):
    return render(request,'appcoder/busqueda_cursos.html')

def resultados_busqueda(request):
    nombre_curso = request.GET['nombre_curso']
    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request,'appcoder/resultado_busqueda.html',{'cursos':cursos})
def entregables(request):
    return render(request,'appcoder/entregables.html')

def eliminar_curso(request,id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('coder-cursos')

def editar_curso(request,id):
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        formulario = CursoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            curso.nombre = data['nombre']
            curso.camada = data['camada']
            curso.save()
            return redirect('coder-cursos')
        else:
            return render(request, 'appcoder/editar_curso.html',{'formulario':formulario,'errores':formulario.errors})
    else:
        formulario = CursoFormulario(initial={'nombre':curso.nombre,'camada':curso.camada})
        return render(request, 'appcoder/editar_curso.html',{'formulario':formulario,'errores':''})

class EntregablesList(LoginRequiredMixin,ListView):
    model = Entregable
    template_name = 'appcoder/list_entregable.html'

class EntregableDetail(DetailView):
    model = Entregable
    template_name= 'appcoder/detail_entregable.html'

class EntregableCreate(CreateView):
    model = Entregable
    success_url= "/coder/entregables"
    fields= ['nombre','fechaDeEntrega','entregado']

class EntregableUpdate(UpdateView):
    model = Entregable
    success_url= '/coder/entregables'
    fields= ['nombre','fechaDeEntrega','entregado']

class EntregableDelete(DeleteView):
    model = Entregable
    success_url= 'coder/entregables/'

def iniciar_sesion(request):
    
    errors = ''
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request,data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            user = authenticate(username=data['username'],password=data['password'])

            if user is not None:
                login(request,user)
                return redirect('coder-inicio')
            else:
                return render(request,'appcoder/login.html',{'formulario':formulario,'errors':"Credenciales invalidas"})

    formulario = AuthenticationForm()
    return render(request,'appcoder/login.html',{'formulario': formulario})

def registrar_usuario(request):
    if request.method == 'POST':
        formulario = userRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('coder-inicio')
        else:
            return render(request,'appcoder/register.html',{'formulario':formulario,'errors':formulario.errors})
    formulario = userRegisterForm()
    return render(request,'appcoder/register.html',{'formulario':formulario})
