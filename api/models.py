from django.db import models

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
