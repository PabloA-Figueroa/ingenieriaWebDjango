from django.contrib import admin
from camaraComercio.models import camarita

admin.site.register(camarita)
class PostAdmin(admin.ModelAdmin):
    list_display = ['campo_1 ', 'campo_2']

# Register your models here.
