from django.contrib import admin
from comentarios.models import comentarios

@admin.register(comentarios)
class comentariosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'contenido']


# Register your models here.
