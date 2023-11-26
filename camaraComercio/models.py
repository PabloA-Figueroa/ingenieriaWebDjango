from django.db import models


class camarita(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=100)
# Create your models here.
