from rest_framework import viewsets
from .serializers import ProductoSerializer
from .models import Producto
from django.shortcuts import render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from crud.models import *
from .serializers import *

from django.http.response import JsonResponse
# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

@api_view(['GET','POST','DELETE'])
def producto_list(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        
        id = request.query_params.get('id',None)
        if id is not None:
            producto = producto.filter(id__contains=id)

        img = request.query_params.get('studio',None)
        if img is not None:
            producto = producto.filter(studio__contains=img)

        titulo = request.query_params.get('titulo',None)
        if titulo is not None:
            producto = producto.filter(titulo__contains=titulo)
        
        descripcion = request.query_params.get('descripcion',None)
        if descripcion is not None:
            producto = producto.filter(descripcion__contains=descripcion)

        stock = request.query_params.get('stock',None)
        if stock is not None:
            producto = producto.filter(stock__contains=stock)

        precio = request.query_params.get('precio',None)
        if precio is not None:
            producto = producto.filter(precio__contains=precio)

        created_at = request.query_params.get('created_at',None)
        if created_at is not None:
            producto = producto.filter(created_at__contains=created_at)

        producto_serializer = ProductoSerializer(producto,many=True)
        return Response(producto_serializer.data)       

    
    elif request.method == 'POST':
        producto_data = JSONParser().parse(request)
        producto_serializer = ProductoSerializer(data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return JsonResponse(producto_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(producto_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cantidad = Producto.objects.all().delete()
        return Response({'mensajes':'Se han eliminado {} productos de la base de datos'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)