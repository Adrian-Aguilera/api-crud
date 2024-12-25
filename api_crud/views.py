from rest_framework import viewsets
from rest_framework.response import Response
from .models import usuario
from .serializer import usuarioSerializer, usuarioSerializerList
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class crudUsuarioViewSet(viewsets.ModelViewSet):

    serializer_class = usuarioSerializer
    @swagger_auto_schema(responses={201: usuarioSerializer})
    def create(self, request):
        data = request.data
        serilizer = usuarioSerializer(data=data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=201)
        return Response(serilizer.errors, status=400)

    def list(self, request):
        data = usuario.objects.all()
        serializer = usuarioSerializerList(data, many=True)
        return Response(serializer.data)