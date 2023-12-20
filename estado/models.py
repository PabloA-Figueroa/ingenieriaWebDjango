from django.db import models
from users.models import User
# Crear un modelos de estado que tenga 6 campos numericos
class Estado(models.Model):
    fecha = models.DateField()
    precioVentaPorUnidad = models.IntegerField()
    cantidadProyectada = models.IntegerField()
    ingresosAdicionales = models.IntegerField()
    costoPorUnidad = models.IntegerField()
    gastosOperativos = models.IntegerField()
    gastosMarketing = models.IntegerField()
    gastosDesarrollo = models.IntegerField()
    # Gastos adicionales es una variable entera y pueda ser nula
    gastosAdicionales = models.IntegerField(null=True, blank=True)
    ingresos = models.IntegerField()
    gastos = models.IntegerField()
    beneficios = models.IntegerField(null=True, blank=True)
    usuario = models.ManyToManyField(User,blank=True)
    # Asignar a este modelo el id de usuario


