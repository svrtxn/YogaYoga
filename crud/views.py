from django.shortcuts import render, redirect, reverse
from crud.forms import ProductForm
from crud.models import Producto, Contacto
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from .forms import *
from .models import Clase
from .forms import ClaseForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            id = form.cleaned_data.get('id')
            titulo = form.cleaned_data.get('titulo')
            precio = form.cleaned_data.get('precio')
            stock = form.cleaned_data.get('stock')
            img = form.cleaned_data.get('img')
            descripcion = form.cleaned_data.get('descripcion')
            nuevo_prod = Producto.objects.create(
                id = id,
                titulo = titulo,
                precio = precio,
                stock = stock,
                img = img,
                descripcion = descripcion
            )
            nuevo_prod.save()
            return redirect(reverse('tienda') + '?creado')
        else:
            print(form.errors)
            return redirect(reverse('tienda') + '?error')
    else:    
        form = ProductForm()
        context = {'form': form }
        context['messages'] = messages.get_messages(request)

    return render(request,'core/form.html', context)



def prod_edit(request,producto_id):
    try:
        producto = Producto.objects.get(id = producto_id)
        form = ProductForm(instance=producto)

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('tienda') + '?UPDATED')
            else:
                return redirect(reverse('producto-edit', args=[producto_id]))

        context = {'form':form}
        return render(request,'core/edit.html',context)
    except:
        print("Error al obtener el producto")
        return redirect(reverse('tienda') + '?NO_EXIST')


def prod_delete(request,producto_id):
    try:
        producto = Producto.objects.get(id = producto_id)
        producto.delete()
        return redirect(reverse('tienda') + '?DELETED')
    except:
        return redirect(reverse('tienda') + '?FAIL')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
    else:
        form = UserRegisterForm()

    context = { 'form' : form}
    return render(request, 'core/register.html', context)

def login(request):
    return render(request, 'core/login.html')

def agregarContacto(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        asunto = request.POST.get('asunto')
        comentarios = request.POST.get('comentarios')

        if usuario and nombre and apellido and telefono and correo and asunto and comentarios:
            contacto = Contacto(
                user=usuario,
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                correo=correo,
                asunto=asunto,
                comentarios=comentarios
            )
            contacto.save()
            return render(request, 'core/index.html')
        else:
            return HttpResponse('Datos de contacto incompletos')
    else:
        return render(request, 'core/contacto.html')


def listarContactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'core/config.html', {'contactos': contactos})

def eliminarContacto(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    contacto.delete()
    return redirect('config')

def admin_clases(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_clases')
    else:
        form = ClaseForm()
    
    clases = Clase.objects.all()
    
    context = {
        'clases': clases,
        'form': form,
    }
    
    return render(request, 'adminClases.html', context)







