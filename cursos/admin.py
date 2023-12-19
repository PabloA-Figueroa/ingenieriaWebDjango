from django.contrib import admin
from cursos.models import Curso, Tema, ContenidoCurso

#@admin.register(Tema)
#class TemaAdmin(admin.ModelAdmin):
 #   list_display = ['nombre']
  #  search_fields = ['nombre']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
   # def display_temas(self, obj):
    #    return ', '.join([tema.nombre for tema in obj.temas.all()])

   # display_temas.short_description = 'Temas'
    list_display = ['titulo', 'contenido']
    search_fields = ['titulo', 'contenido']
    #filter_horizontal = ['temas']


@admin.register(ContenidoCurso)
class ContenidoCursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'pieImagen']
    search_fields = ['titulo', 'pieImagen']
    filter_horizontal = ['cursos']
