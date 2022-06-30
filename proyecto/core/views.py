from ast import If
from dataclasses import dataclass
from email import message
from pyexpat.errors import messages
from django.http import Http404
from django.shortcuts import redirect, render,get_object_or_404
from .forms import UsuarioForm,ProductoForm,CustomUserCreationForm
from .models import Usuario,Producto
from django.contrib.auth import authenticate,login
from django.contrib import messages
from rest_framework import viewsets
from .serialazers import ProductoSerialaizer
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
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

    return render(request,'core/tienda.html',datos)

def iniciarSesion(request, id):
    usuario=Usuario.objects.get(id_usuario=id)
    datos={
        'form':UsuarioForm(instance=usuario)
    }
    return render(request,'core/iniciarSesion.html',datos)

@permission_required('core.add_producto')
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
    
@permission_required('core.change_producto')
def carrito(request):
    producto = Producto.objects.all()
    page = request.GET.get('page',1)

    ##try:
        ##paginator=Paginator(producto, 3)
        ##producto=paginator.page(page)
    #except:
     #   raise Http404

    datos={
        'entity':producto,
       ## 'paginator':paginator
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

def eliminar_producto(request, id):
    producto=get_object_or_404(Producto, id_producto=id)
    producto.delete()
    return redirect(to="carrito")


def usuarios(request):
    return render(request, 'core/usuarios.html')



class ProductoViewset(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class=ProductoSerialaizer

    def get_queryset(self):
        productos=Producto.objects.all()

        nombre=self.request.GET.get('nombre')

        if nombre:
            productos= productos.filter(nombre_producto__contains=nombre)
        
        return productos