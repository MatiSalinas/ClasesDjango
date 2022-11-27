from django.urls import path
from appcoder.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('estudiantes',estudiantes,name='coder-estudiantes'),
    path('profesores/',profesores,name='coder-profesores'),
    path('profesores/crear',creacion_profesores,name='coder-profesores-crear'),
    path('cursos/',cursos,name='coder-cursos'),
    path('cursos/borrar/<id>',eliminar_curso,name='coder-cursos-borrar'),
    path('cursos/actualizar/<id>',editar_curso,name='coder-cursos-editar'),
    path('cursos/buscar/',buscar_curso,name='coder-cursos-buscar'),
    path('cursos/buscar/resultado',resultados_busqueda,name='coder-cursos-resultados'),
    path('entregables/',EntregablesList.as_view(),name='coder-entregables'),
    path('entregables/detalle/<pk>',EntregableDetail.as_view(),name='coder-entregables-detail'),
    path('entregables/crear/',EntregableCreate.as_view(),name='coder-entregables-create'),
    path('entregables/actualizar/<pk>',EntregableUpdate.as_view(),name='coder-entregables-update'),
    path('entregables/borrar/<pk>',EntregableDelete.as_view(),name='coder-entregables-delete'),
    path('',inicio,name='coder-inicio'),
    path('login/',iniciar_sesion, name = 'auth-login'),
    path('register',registrar_usuario,name='auth-register'),
    path('logout',LogoutView.as_view(template_name='appcoder/logout.html'),name='auth-logout'),

]
