from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.Serializer):

    class Meta:
        model = Usuario
        fields = '__all__'