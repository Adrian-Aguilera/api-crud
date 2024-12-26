from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import usuario
from .serializer import usuarioSerializer, usuarioSerializerList
from .Methods import Methods
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

@swagger_auto_schema(responses={201: usuarioSerializer})
class crudUsuarioViewSet(viewsets.ModelViewSet):

    serializer_class = usuarioSerializerList
    queryset = usuario.objects.all()

class  EjerciciosViews(APIView):
    @api_view(['POST'])
    def isPalindromo(request):
        if request.method == 'POST':
            data = request.data
            palabra = data.get('palabra')
            if palabra:
                return Response({'resultado': {'mensaje': "es una palabra palindroma"} if Methods.es_palindromo(palabra) else { 'error': 'No es palindromo'}})
            else:
                return Response({'error': 'No se ha introducido la palabra'})
        else:
            return Response({'errors':{
                'error': 'Metodo no permitido'
            }})