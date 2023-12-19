from django.contrib import admin
from estado.models import Estado
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('precioVentaPorUnidad', 'cantidadProyectada', 'ingresosAdicionales', 'costoPorUnidad', 'gastosOperativos', 'gastosMarketing', 'gastosDesarrollo', 'tasaCrecimiento', 'duracionProyeccion', 'gastosAdicionales', 'ingresos', 'gastos', 'proyecciones', 'beneficios')
    search_fields = ['usuario']
    #filter_horizontal = ['temas']
# Register your models here.
