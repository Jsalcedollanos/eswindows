from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from registros.models import *
from django.core.paginator import Paginator
from django.contrib import messages
from registros.form import FormCliente, FormOrden
from django.template import loader
from django.urls import reverse
from django.views.generic import (View, TemplateView, ListView, DetailView)
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/index.html',{
        'clientes':clientes,
    })

def editarCliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    template = loader.get_template('clientes/editCliente.html')
    context = {
        'cliente':cliente
    }

    return HttpResponse(template.render(context, request))

def updateCliente(request, id):
  nombre = request.POST['nombre']
  direccion = request.POST['direccion']
  telefono = request.POST['telefono']
  nacionalidad = request.POST['nacionalidad']
  correo = request.POST['correo']
  cliente = Cliente.objects.get(id=id)
  cliente.nombre = nombre
  cliente.direccion = direccion
  cliente.telefono = telefono
  cliente.nacionalidad = nacionalidad
  cliente.correo = correo
  cliente.save()
  return HttpResponseRedirect(reverse('clientes'))

def eliminarCliente(request, id):
  cliente = Cliente.objects.get(id=id)
  cliente.delete()
  return HttpResponseRedirect(reverse('clientes'))

def addCliente(request):

    if request.method == 'POST':
        formulario = FormCliente(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            identificacion = data_form.get('identificacion')
            nombre    =     data_form.get('nombre')
            direccion  =     data_form.get('direccion')
            telefono   =     data_form.get('telefono')
            nacionalidad   =     data_form.get('nacionalidad')
            correo   =     data_form.get('correo')
            cliente = Cliente(
                identificacion = identificacion,
                nombre = nombre,
                direccion = direccion,
                telefono = telefono,
                nacionalidad = nacionalidad,
                correo = correo
            )
            cliente.save()
            # Crear mensaje flash
            messages.success(request, f'Has creado correctamente el cliente')
            formulario = FormCliente()
        else:
            messages.error(request, f'Error al guardar el cliente, revisa sus datos.')

    else:
        formulario = FormCliente()
    return render(request, 'clientes/addCliente.html',{
        'form' : formulario,
    })

def ordenes(request):
    ordenes = Orden.objects.all()
    
    return render(request, 'ordenes/index.html',{
        'ordenes':ordenes,
    })
def addOrden(request):
  orden = Cliente.objects.all()
  template = loader.get_template('ordenes/addOrden.html')
  return HttpResponse(template.render({'orden':orden}, request))

def crearOrden(request):
    
    cliente_id = request.POST['cliente_id']
    detalle = request.POST['detalle']
    orden = Orden(cliente_id=cliente_id, detalle=detalle)
    orden.save()
    return HttpResponseRedirect(reverse('ordenes'))

def eliminarOrden(request, idOrden):
  orden = Orden.objects.get(idOrden=idOrden)
  orden.delete()
  return HttpResponseRedirect(reverse('ordenes'))

def cargarOrden(request, idOrden):
    orden = Orden.objects.get(pk=idOrden)
    template = loader.get_template('ordenes/editarOrden.html')
    context = {
        'orden':orden
    }

    return HttpResponse(template.render(context, request))

def updateEstado(request, idOrden):
  estado = request.POST['estado']
  orden = Orden.objects.get(idOrden=idOrden)
  orden.estado = estado
  orden.save()
  return HttpResponseRedirect(reverse('ordenes'))




