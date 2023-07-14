from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from crud.models import Producto
           
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'core/tienda.html', {'productos': productos, 'user': request.user})

def posturas(request):
    return render(request, 'core/posturas.html')
def sucursales(request):
    return render(request, 'core/sucursales.html')
def yoga(request):
    return render(request, 'core/clases.html')
def nosotros(request):
    return render(request, 'core/nosotros.html')
