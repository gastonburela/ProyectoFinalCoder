from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.test import Client
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.db.models import Q
from collections import namedtuple

from django.core.exceptions import FieldError
from django.db import DEFAULT_DB_ALIAS, DatabaseError
from django.db.models.constants import LOOKUP_SEP

from django.utils import tree
from WebFinal.forms import Formulario_cliente
from WebFinal.models import *
from WebFinal.forms import *
# Create your views here.

def inicio(request):

    return render(request, 'inicio2.html')

# def form_cliente(request):

#     #CREATE
    
#     if request.method == 'POST':

#         add_cliente = Formulario_cliente(request.POST)
        
#         if add_cliente.is_valid():

#             datos = add_cliente.cleaned_data
#             nuevo_cliente = Cliente(nombre=datos['nombre'], apellido=datos['apellido'], telefono=datos['telefono'], direccion=datos['direccion'])
#             nuevo_cliente.save()
#             return render(request, 'cliente_creado.html', {'mensaje':'Cliente creado con exito.'})
        
#     else:
#         add_cliente = Formulario_cliente()

#     return render(request, 'form_cliente.html', {'add_cliente': add_cliente})


class CrearCliente(CreateView):

    model = Cliente
    form_class = Formulario_cliente
    template_name = 'form_cliente.html'
    success_url = '/WebFinal/crear_exito/'


    #READ
# def lista_clientes(request):

#     clientes = Cliente.objects.all()

#     return render(request, "lista_clientes.html", {"clientes": clientes})

def creado_con_exito(request):

    return render(request,'crear_exito.html')

class Mostrar_clientes(ListView):

    model = Cliente
    template_name = "lista_clientes.html"
    context_object_name = "clientes"
    #EDIT

# def borracliente(request, id):

#     if request.method == 'POST':

#         cliente = Cliente.objects.get(id=id)
#         cliente.delete()

#         clientes = Cliente.objects.all()

#         return render(request, "lista_clientes.html", {"clientes": clientes})  

class Detalle_cliente(DetailView):

    model = Cliente
    template_name = "detalle_cliente.html"
    context_object_name = "cliente"

class EditarCliente(UpdateView):

    model = Cliente
    template_name = "cliente_update.html"
    fields = ('__all__')
    success_url = '/WebFinal/exito_update/'

def cliente_actualizado(request):

    return render(request,'exito_update.html')

class Borracliente(DeleteView):

        model = Cliente
        template_name = 'borrarcliente.html'
        success_url = '/WebFinal/lista_clientes'
#BUSQUEDA
def busqueda_cliente(request):
    
    return render(request, 'busqueda_cliente.html')

class BuscaCliente(ListView):
    model = Cliente
    template_name = "busqueda_cliente.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("dni")
        if query=="":
            response = 'Cliente no encontrado'
            HttpResponseRedirect('/WebFinal/', {'response':response})
        else:    
            object_list = Cliente.objects.filter(Q(dni__icontains=query))       
            return (object_list)
        
# def editar_cliente(request, id):

#     print('method:', request.method)
#     print('post: ', request.POST)

#     cliente = Cliente.objects.get(id=id)

#     if request.method == 'POST':

#         cliente_edit = Formulario_cliente(request.POST)

#         if cliente_edit.is_valid():

#             datos = cliente_edit.cleaned_data

#             cliente.nombre = datos["nombre"]
#             cliente.apellido = datos["apellido"]
#             cliente.telefono = datos["telefono"]
#             cliente.direccion = datos["direccion"]

#             cliente.save()

#             return HttpResponseRedirect('/WebFinal/lista_clientes/')
    
#     else:

#         cliente_edit = Formulario_cliente(initial={
#             "nombre": cliente.nombre,
#             "apellido": cliente.apellido,
#             "telefono": cliente.telefono,
#             "direccion": cliente.direccion,
#         })

#         return render(request, "editarcliente.html", {"cliente_edit": cliente_edit, "id": cliente.id})


# def form_empleado(request):
#     #cuerpo 
#     return render(request, 'form_empleado')

class Empleados(CreateView):

    model = Empleado
    form_class = Formulario_empleado
    template_name = 'crea_empleado.html'
    success_url = '/WebFinal/exito_empleado/'
    


def empleado_creado(request):

    return render(request, 'exito_empleado.html')

class MostrarEmpleados(ListView):

    model = Empleado
    form_class = Formulario_empleado
    template_name = 'lista_empleados.html'
    context_object_name = "empleados"

class Detalle_Empleado(DetailView):

    model = Empleado
    template_name = "detalle_empleado.html"
    context_object_name = "empleado"

class BorraEmpleado(DeleteView):

        model = Empleado
        template_name = 'borrarempleado.html'
        success_url = '/WebFinal/lista_empleados'

class EditarEmpleado(UpdateView):

    model = Empleado
    template_name = "empleado_update.html"
    fields = ('__all__')
    success_url = '/WebFinal/exito_update_empleado/'

def empleado_actualizado(request):

    return render(request, 'exito_update_empleado.html')

#BUSQUEDA
def busqueda_empleado(request):
    
    return render(request, 'busqueda_empleado.html')

class BuscarEmpleado(ListView):
    model = Empleado
    template_name = "busqueda_empleado.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("apellido")
        
        if query=='':
            response = 'Empleado no encontrado'
            HttpResponseRedirect('/WebFinal/resultado_empleado/', {'response':response})
        else:    
            object_list = Empleado.objects.filter(Q(apellido__icontains=query))       
            return (object_list)
# PRODUCTOS

class CrearProducto(CreateView):

    model = Productos
    form_class = Formulario_productos
    template_name = 'crea_producto.html'
    success_url = '/WebFinal/exito_producto/'

def productocreado(request):

    return render(request, 'exito_producto.html')

class ListaProductos(ListView):

    model = Productos
    form_class = Formulario_productos
    template_name = 'lista_productos.html'
    context_object_name = "productos"

class Detalle_Producto(DetailView):

    model = Productos
    template_name = "detalle_producto.html"
    context_object_name = "producto"

class BorraProducto(DeleteView):

        model = Productos
        template_name = 'borrarproducto.html'
        success_url = '/WebFinal/lista_productos'

class EditarProducto(UpdateView):

    model = Productos
    template_name = "producto_update.html"
    fields = ('__all__')
    success_url = '/WebFinal/exito_update_producto/'

def producto_actualizado(request):

    return render(request, 'exito_update_producto.html')

#BUSQUEDA
def busqueda_producto(request):
    
    return render(request, 'busqueda_producto.html')

class BuscarProducto(ListView):
    model = Productos
    template_name = "busqueda_producto.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("modelo")
        if query=="":
            response = 'Producto no encontrado'
            HttpResponseRedirect('/WebFinal/', {'response':response})
        else:    
            object_list = Productos.objects.filter(Q(modelo__icontains=query))       
            return (object_list)
# def form_productos(request):
#     #cuerpo 

#     return render(request, 'form_productos')

# PROVEEDORES

class CrearProveedor(CreateView):

    model = Proveedores
    form_class = Formulario_proveedores
    template_name = 'crea_proveedor.html'
    success_url = '/WebFinal/exito_proveedor/'

def proveedorcreado(request):

    return render(request, 'exito_proveedor.html')

class ListaProveedores(ListView):

    model = Proveedores
    form_class = Formulario_proveedores
    template_name = 'lista_proveedores.html'
    context_object_name = "proveedores"

class Detalle_Proveedor(DetailView):

    model = Proveedores
    template_name = "detalle_proveedor.html"
    context_object_name = "proveedor"

class BorraProveedor(DeleteView):

        model = Proveedores
        template_name = 'borrarproveedor.html'
        success_url = '/WebFinal/lista_proveedores'

class EditarProveedor(UpdateView):

    model = Proveedores
    template_name = "proveedor_update.html"
    fields = ('__all__')
    success_url = '/WebFinal/exito_update_proveedor/'

def proveedor_actualizado(request):

    return render(request, 'exito_update_proveedor.html')


#BUSQUEDA
def busqueda_proveedor(request):
    
    return render(request, 'busqueda_proveedor.html')

class BuscarProveedor(ListView):
    model = Proveedores
    template_name = "busqueda_proveedor.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("nombre")
        if query=="":
            response = 'Proveedor no encontrado'
            HttpResponseRedirect('/WebFinal/', {'response':response})
        else:    
            object_list = Proveedores.objects.filter(Q(nombre__icontains=query))       
            return (object_list)

# def form_proveedores(request):
#    #cuerpo 

#     return render(request, 'form_proveedores')

def login(request):

    if request.method=='POST':

        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():

            datos = formulario.cleaned_data

            usuario = datos['username']
            psw = datos['password']

            user = authenticate(username=usuario, password=psw)

            if user:

                login(request, user)

                return render(request, 'inicio2.html', {'mensaje': f'Bienvenido {user}'})
            
            else:

                return render(request, 'inicio2,html', {'mensaje': f'Usuario o contraseña incorrectos.'})

        else:

            return render(request, 'inicio2,html', {'mensaje': f'Formulario inválido.'})

        