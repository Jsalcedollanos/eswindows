"""eswindows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from registros import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name="dashboard"),
    path('clientes/', views.clientes, name="clientes"),
    path('ordenes/', views.ordenes, name="ordenes"),
    path('clientes/crear', views.addCliente, name="addCliente"),
    path('clientes/editar/<int:id>', views.editarCliente, name="editCliente"),
    path('clientes/eliminar/<int:id>', views.eliminarCliente, name="eliminarCliente"),
    path('clientes/update/<int:id>', views.updateCliente, name="updateCliente"),
    path('add/orden', views.addOrden, name="addOrden"),
    path('crear/orden', views.crearOrden, name="crearOrden"),
    path('eliminar/orden/<int:idOrden>', views.eliminarOrden, name="eliminarOrden"),
    path('orden/editar/<int:idOrden>', views.cargarOrden, name="cargarOrden"),
    path('orden/update/<int:idOrden>', views.updateEstado, name="updateEstado"),


    


]
