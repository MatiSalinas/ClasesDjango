from django.urls import path
from appcoder.views import *
urlpatterns = [
    path('estudiantes',estudiantes,name='coder-estudiantes'),
    path('profesores/',profesores,name='coder-profesores'),
    path('cursos/',cursos,name='coder-cursos'),
    path('entregables/',entregables,name='coder-entregables'),
    path('',inicio,name='coder-inicio')

]
