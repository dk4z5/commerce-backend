from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from rest_framework import generics, status
from rest_framework.response import Response

from .models import Venda, Preco, RetiradaProduto
from .serializers import VendaSerializer, RetiradaProdutoSerializer, PrecosSerializer


class VendasView(generics.ListCreateAPIView):
    queryset = Venda.objects.all().order_by('-id')
    serializer_class = VendaSerializer

    def perform_create(self, serializer):
        produtos = serializer.validated_data.pop('produtos')
        venda = serializer.save(preco_total=0)

        preco = 0.0
        for prod in produtos:
            ret = RetiradaProduto(produto=prod['produto'], quantidade=prod['quantidade'], venda=venda, desconto=prod['desconto'])
            preco += prod['produto'].preco_base * prod['quantidade']
            print(prod['quantidade'])
            if prod['desconto'] != None:
                preco = preco*(1 - prod['desconto']/100)
            #hook direto na model.
            ret.save()
        
        if preco > 0:
            venda.preco_total = preco
            venda.save()

class RetiradaProdutoView(generics.ListCreateAPIView):
    queryset = RetiradaProduto.objects.all().order_by('-id')
    serializer_class = RetiradaProdutoSerializer


class PrecosView(generics.ListCreateAPIView):
    queryset = Preco.objects.all().order_by('-id')
    serializer_class = PrecosSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        prod = data['produto']
        
        prod.preco_base = data['valor']
        prod.save()
        serializer.save(data_alteracao=timezone.now())
