from rest_framework.serializers import ModelSerializer
from comentarios.models import comentarios

class postSerializer(ModelSerializer):
    class Meta:
        model = comentarios
        fields = ['id','titulo' , 'contenido' , 'contenidoFinal' ]