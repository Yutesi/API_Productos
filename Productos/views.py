from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las categorías de productos.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los productos.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
