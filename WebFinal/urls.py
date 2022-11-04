from django.urls import path
from .views import *


urlpatterns = [
    path('inicio2/', inicio, name='inicio2'),
   # path('form_proveedores/', form_proveedores, name='form_proveedores'),
    #path('form_productos/', form_productos, name='form_productos'),
    path('form_cliente/', CrearCliente.as_view(), name='form_cliente'),  
    #path('cliente_creado/', form_cliente, name='clientecreado'),
    path('lista_clientes/', Mostrar_clientes.as_view(), name='lista_clientes'),
    path('borra_cliente/<pk>', Borracliente.as_view(), name='borracliente'),
    #path('editar-cliente/<int:id>', editar_cliente, name='editarcliente'),
    path('crear_exito/', creado_con_exito, name='crear_exito'),
    path('exito_update/', cliente_actualizado, name='clienteactualizado'),
    path('detalle_cliente/<pk>', Detalle_cliente.as_view(), name='detalle_cliente'),
    path('clienteupdate/<pk>', EditarCliente.as_view(), name='clienteupdate'),
    path('crear_empleado/', Empleados.as_view(), name='crea_empleado'),
    path('exito_empleado/',empleado_creado,name='exito_empleado'),
    path('detalle_empleado/<pk>',Detalle_Empleado.as_view(),name='detalle_empleado'),
    path('lista_empleados/', MostrarEmpleados.as_view(), name='lista_empleados'),
    path('borra_empleado/<pk>', BorraEmpleado.as_view(), name='borraempleado'),
    path('empleadoupdate/<pk>', EditarEmpleado.as_view(), name='empleadoupdate'),
    path('exito_update_empleado/', empleado_actualizado, name='empleadoactualizado'),
    
    path('crear_producto/', CrearProducto.as_view(), name='crear_producto'),  
    path('exito_producto/', productocreado, name='productocreado'),
    path('lista_productos/', ListaProductos.as_view(), name='lista_productos'),
    path('detalle_producto/<pk>',Detalle_Producto.as_view(),name='detalle_producto'),
    path('borra_producto/<pk>', BorraProducto.as_view(), name='borraproducto'),
    path('productoupdate/<pk>', EditarProducto.as_view(), name='productoupdate'),
    path('exito_update_producto/', producto_actualizado, name='productoactualizado'),
    
    path('crear_proveedor/', CrearProveedor.as_view(), name='crear_proveedor'), 
    path('exito_proveedor/', proveedorcreado, name='proveedorcreado'),
    path('lista_proveedores/', ListaProveedores.as_view(), name='lista_proveedores'),
    path('detalle_producto/<pk>',Detalle_Proveedor.as_view(),name='detalle_proveedor'),
    path('borra_proveedor/<pk>', BorraProveedor.as_view(), name='borraproveedor'),
    path('proveedorupdate/<pk>', EditarProveedor.as_view(), name='proveedorupdate'),
    path('exito_update_proveedor/', proveedor_actualizado, name='proveedoractualizado'),


]
