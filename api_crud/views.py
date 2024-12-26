from rest_framework import viewsets
from rest_framework.response import Response
from .models import usuario
from .serializer import usuarioSerializer, usuarioSerializerList
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

@swagger_auto_schema(responses={201: usuarioSerializer})
class crudUsuarioViewSet(viewsets.ModelViewSet):

    serializer_class = usuarioSerializerList
    queryset = usuario.objects.all()