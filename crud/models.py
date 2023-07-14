from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Producto(models.Model):
    id = models.BigAutoField (primary_key = True)
    img = models.ImageField(verbose_name="imagen", upload_to="productos", default="", blank=True, null=True)
    titulo = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(verbose_name='Descripcion', max_length=40, default="")
    stock = models.IntegerField(verbose_name='Stock')
    precio = models.IntegerField(verbose_name='Precio')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creción') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de actualización')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['created_at']
    
    def __str__(self):
        return self.titulo
    

class Contacto(models.Model):
    id= models.BigAutoField(primary_key = True)
    user = models.CharField(max_length=50, verbose_name='Usuario')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    telefono = models.IntegerField(verbose_name='Telefono')
    correo = models.EmailField(verbose_name='Correo electronico')
    asunto = models.CharField(max_length=50, verbose_name='Asunto')
    comentarios = models.TextField(max_length=300, verbose_name='Comentarios')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion', null=True)

    def __str__(self):
        return self.asunto + ' - ' + self.user
                                   
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cupo_maximo = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Otros campos que puedas necesitar
    
    def __str__(self):
        return self.nombre
