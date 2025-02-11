from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def hola_mundo(request):
#     return HttpResponse("¡Hola, mundo desde Django!")


from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
