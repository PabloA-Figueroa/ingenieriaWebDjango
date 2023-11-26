from django.db import models

# Create your models here.
class comentarios(models.Model):
    titulo= models.CharField(max_length=100)
    contenido= models.CharField(max_length=100)
    contenidoFinal= models.CharField(max_length=800)

# Create your models here.
