from django.db import models
from ckeditor.fields import RichTextField


class Tema(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='temas/', null=True, blank=True)
    def __str__(self):
        return self.nombre
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    temas = models.ManyToManyField(Tema, blank=True)
    def __str__(self):
        return self.titulo

class ContenidoCurso(models.Model):
    titulo = models.CharField(max_length=400)
    pieImagen = models.CharField(max_length=400)
    concepto = RichTextField(blank=True, null=True)
    ejemplo1 = RichTextField(blank=True, null=True)
    ejemplo2= RichTextField(blank=True, null=True)
    ejemplo3= RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='contenidos/', blank=True, null=True)
    cursos = models.ManyToManyField(Curso, blank=True)
