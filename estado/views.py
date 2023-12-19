from django.shortcuts import render
from estado.models import Estado
from estado.serializers import EstadoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class EstadoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EstadoSerializer

    def get_queryset(self):
        return Estado.objects.filter(usuario=self.request.user)
