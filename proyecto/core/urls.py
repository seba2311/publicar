import imp
from unicodedata import name
from xml.dom.minidom import Document
from django.conf import settings
from django.urls import URLPattern, path, include
from .views import home,quienesSomos,registro,tienda,iniciarSesion,tienda2,carrito,modificar_producto,usuarios,base,ProductoViewset,eliminar_producto
from rest_framework import routers
from django.contrib.staticfiles.urls import static

router= routers.DefaultRouter()
router.register('producto',ProductoViewset)

urlpatterns=[
    path('',home,name="home"),
    path('quienesSomos/',quienesSomos,name="quienesSomos"),
    path('registro/',registro,name="registro"),
    path('tienda/',tienda,name="tienda"),
    path('iniciar_sesion/<id>',iniciarSesion,name="iniciarSesion"),
    path('tienda2/',tienda2,name="tienda2"),
    path('carrito/',carrito,name='carrito'),
    path('modificar-producto/<id>/',modificar_producto,name='modificar_producto'),
    path('usuarios',usuarios,name="usuarios"),
    path('base',base,name='base'),
    path('api/',include(router.urls)),
    path('eliminar-producto/<id>/',eliminar_producto,name="eliminar_producto")
]