from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class ProductForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id',
            'titulo',
            'precio',
            'stock',
            'img',
            'descripcion'
        ]
        labels = {
            'id':'ID',
            'titulo':'TITULO',
            'precio':'PRECIO',
            'stock':'STOCK',
            'img':'IMAGEN',
            'descripcion': 'DESCRIPCION'
        }
        widgets = {
            'id':forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'titulo':forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'precio':forms.TextInput(attrs={'class':'form-control shadow-none no-arrows','type':'number'}),
            'stock':forms.TextInput(attrs={'class':'form-control shadow-none no-arrows','type':'number'}),
            'img':forms.FileInput(attrs={'class':'form-control shadow-none'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control shadow-none'})
        }

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = [
            'user',
            'nombre',
            'apellido',
            'telefono',
            'correo',
            'asunto',
            'comentarios'
        ]
        labels = {
            'user': 'Usuario',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Telefono',
            'correo': 'Correo',
            'asunto': 'Asunto',
            'comentarios': 'Comentarios',
            
        }
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'nombre':forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'apellido':forms.TextInput(attrs={'class':'form-control shadow-none no-arrows'}),
            'telefono':forms.TextInput(attrs={'class':'form-control shadow-none no-arrows','type':'number'}),
            'correo':forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'asunto':forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'comentarios':forms.TextInput(attrs={'class':'form-control shadow-none'})
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_text = {k:"" for k in fields }

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'