from rest_framework import serializers
from .models import Venda, Preco, RetiradaProduto
from estoque.models import Produto

class RetiradaProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = RetiradaProduto
        fields = '__all__'
        read_only_fields=['venda']
    

class VendaSerializer(serializers.ModelSerializer):

    produtos = RetiradaProdutoSerializer(many=True, required=False)
    class Meta:
        model = Venda
        fields = ['data', 'cliente', 'produtos', 'preco_total', 'id', 'desconto', 'recebido']
        read_only_fields=['preco_total', 'id']

class PrecosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Preco
        fields = '__all__'
        read_only_fields = ['data_alteracao']
        