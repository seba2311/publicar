from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario=models.IntegerField(primary_key=True, verbose_name="rut del usuario")
    nombre_usuario=models.CharField(max_length=50, verbose_name="nombre usuario")
    correo=models.CharField(max_length=50, verbose_name="correo")
    clave=models.CharField(max_length=30, verbose_name="clave")
    apellido=models.CharField(max_length=50,verbose_name="apellido")
    comuna=models.CharField(max_length=50,verbose_name="comuna")
    def __str__(self):
        
        return self.nombre_usuario

class Categoria(models.Model):
    id_categoria=models.IntegerField(primary_key=True, verbose_name="id de categoria")
    nombre_categoria=models.CharField(max_length=50, verbose_name="nombre de la categoria")
    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    id_producto=models.IntegerField(primary_key=True,verbose_name="id_producto")
    nombre_producto=models.CharField(max_length=50, verbose_name="nombre_producto")
    stock=models.IntegerField(verbose_name="stock")
    descripcion=models.CharField(max_length=100,verbose_name="descripcion")
    precio=models.IntegerField(verbose_name="precio")
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="productos", null=True)
    def __str__(self):
        return self.nombre_producto



