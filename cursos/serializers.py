from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from cursos.models import Curso, Tema, ContenidoCurso


class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class ContenidoCursoSerializer(ModelSerializer):
    class Meta:
        model = ContenidoCurso
        fields = '__all__'
