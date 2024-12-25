from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class crudViewSet(viewsets.ModelViewSet):

    def create(self, request):
        return Response({"message": "Hello"})