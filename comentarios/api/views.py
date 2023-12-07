from rest_framework.viewsets import ViewSet,ModelViewSet
from comentarios.models import comentarios
from comentarios.serializers import postSerializer
from rest_framework.permissions import IsAdminUser

class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = postSerializer
    queryset = comentarios.objects.all()



"""
class ComentariosAPIView(APIView):
    def get(self, request):
        #coments = comentarios.objects.all()
        serializer = postSerializer(comentarios.objects.all(), many=True)
        #coments = [comentarios.titulo for comentarios in comentarios.objects.all()]

        return Response(status=status.HTTP_200_OK,data=serializer.data)


    def post(self, request):
        serializer = postSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = postSerializer(comentarios.objects.all(), many=True)
        #comentarios.objects.create(titulo=request.POST['titulo'], contenido=request.POST['contenido'],
         #                          contenidoFinal=request.POST['contenidoFinal'])
        return Response(status=status.HTTP_200_OK,data=serializer.data)

class ComentariosViewSet(ViewSet):
    def list(self, request):
        serializer = postSerializer(comentarios.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)

    def retrieve(self, request, pk):
        post = postSerializer(comentarios.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK,data=post.data)

    def create(self, request):
        serializer = postSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK,data=serializer.data)
"""


