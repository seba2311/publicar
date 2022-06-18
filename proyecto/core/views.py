
from ast import If
from dataclasses import dataclass
from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render,get_object_or_404

from .forms import UsuarioForm,ProductoForm,CustomUserCreationForm


from .models import Usuario,Producto
from django.contrib.auth import authenticate,login
from django.contrib import messages
from rest_framework import viewsets
from .serialazers import ProductoSerialaizer

# Create your views here.
def home (request):
    usuario = Usuario.objects.all()
    datos = {
        'usuarios':usuario
    }
    return render(request, 'core/home.html',datos)

def base(request):
    return render(request, 'core/base.html')


def quienesSomos (request):
    return render(request, 'core/QuienesSomos.html')


def tienda(request):
    return render(request,'core/tienda.html')

def iniciarSesion(request, id):
    usuario=Usuario.objects.get(id_usuario=id)
    datos={
        'form':UsuarioForm(instance=usuario)
    }
    return render(request,'core/iniciarSesion.html',datos)

def tienda2(request):
    usuario=Usuario.objects.all()
    producto = Producto.objects.all()
    datos ={
        'form':ProductoForm(),
        'productos':producto,
        'usuarios':usuario

    }
    if request.method=="POST":
        formulario=ProductoForm(request.POST, files=request.FILES)
        
        if formulario.is_valid:
            formulario.save()
            messages.success(request,"Agregado correctamente")
        else:
            datos["form"]=formulario

    return render(request,'core/tienda2.html',datos)
    
    
def carrito(request):
    producto = Producto.objects.all()
    datos={
        'productos':producto
    }
    return render(request,'core/carrito.html',datos)


def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="home")

        data['form']=formulario
    return render(request,'registration/registro.html',data)


def modificar_producto(request, id):
    producto=get_object_or_404(Producto, id_producto=id)
    data={
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="carrito")
        data['form']= formulario
    
    return render(request, 'core/modificar.html',data)

def usuarios(request):
    return render(request, 'core/usuarios.html')



class ProductoViewset(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class=ProductoSerialaizer