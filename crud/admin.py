from django.contrib import admin
from .models import Producto, Contacto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):     

    readonly_fields = ('created_at','updated_at')     
    list_display = ('id','titulo','precio','stock')     
    ordering = ['titulo']

admin.site.register(Producto, ProductoAdmin)

admin.site.register(Contacto)