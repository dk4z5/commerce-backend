from rest_framework import serializers
from .models import Estoque, Produto

class EstoqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estoque
        fields = '__all__'

class EstoqueDepthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estoque
        fields = '__all__'
        depth = 1

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'
        read_only_fields = ['data_insercao', 'desconto']