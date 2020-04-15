from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics

from .models import Usuario
from .serializer import UsuarioSerializer

# Create your views here.

class UsuarioView(APIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

