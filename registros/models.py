from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    identificacion = models.CharField(unique=True, null=True, verbose_name="ide", max_length=15)
    nombre = models.CharField(verbose_name="nombre", max_length=30)
    direccion = models.CharField(verbose_name="direccion", max_length=35)
    telefono = models.CharField(verbose_name="telefono", max_length=15)
    nacionalidad = models.CharField(verbose_name="nacionalidad", max_length=25)
    correo = models.CharField(verbose_name="correo", max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Orden(models.Model):
    idOrden = models.BigAutoField(primary_key=True, verbose_name="num_orden")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    detalle = models.CharField(max_length=15, verbose_name="detalle")
    estado = models.CharField(default="Solicitada",verbose_name="estado", max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

