from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(min_length=3,max_length=50)
    apellido = forms.CharField(min_length=3,max_length=50)
    email = forms.EmailField()

class CursoFormulario(forms.Form):
    nombre = forms.CharField(min_length=3)
    camada = forms.IntegerField()

class userRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia' ,widget= forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia' ,widget=forms.PasswordInput)
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    class Meta:
        model = User
        fields = ['username','email','last_name','first_name','password1','password2']