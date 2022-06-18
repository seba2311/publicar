from pyexpat import model
from attr import field
from click import style
from colorama import Style
from django import forms
from django.forms import ModelForm
from .models import Usuario, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields=['id_usuario',
                'nombre_usuario',
                'apellido',
                'clave',
                'correo',
                'comuna']

class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields=['nombre_producto','stock','descripcion','precio','categoria','imagen']
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username',"first_name","last_name","email","password1","password2"]
