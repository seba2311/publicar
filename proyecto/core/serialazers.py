from os import read
from pyexpat import model

from attr import field, fields
from .models import Producto
from rest_framework import serializers

class ProductoSerialaizer(serializers.ModelSerializer):
    nombre_categoria=serializers.CharField(read_only=True, source="categoria.nombre_categoria")
    class Meta:
        model= Producto
        fields='__all__'