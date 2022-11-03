from django.urls import path
from appcoder.views import *
urlpatterns = [
    path('estudiantes',estudiantes),
    path('profesores/',profesores),
    path('cursos/',cursos),
    path('entregables',entregables),
    path('',inicio)

]
