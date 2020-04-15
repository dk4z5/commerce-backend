from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import F

from api import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters

from comserver.pagination import CustomPagination
from .models import Estoque, Produto
from .serializers import EstoqueSerializer, EstoqueDepthSerializer, ProdutoSerializer

from caixa.models import Preco

from api.permissions import AuthAndEmployer

class EstoqueView(generics.ListCreateAPIView):
    permission_classes_by_action = [AuthAndEmployer]
    permission_classes = [AuthAndEmployer]
    queryset = Estoque.objects.all().order_by('-id')
    serializer_class = EstoqueSerializer

    # hook ListModelMixin
    def list_disabled(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = EstoqueDepthSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EstoqueDepthSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        data = serializer.validated_data
        prod = data['produto']
        prod.quantidade += int(data['quantidade'])
        prod.save()
        
        serializer.save()

class EstoqueDepthView(generics.ListAPIView):
    #permission_classes = [AuthAndEmployer]
    permission_classes_by_action = {'POST': [AuthAndEmployer],
                                    'GET': [AuthAndEmployer]}

    queryset = Estoque.objects.all().order_by('-id')
    serializer_class = EstoqueDepthSerializer
    ordering = ['id']

class EstoquePartialView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    
    def perform_update(self, serializer):
        data = self.request.data
        pk = self.kwargs['pk']

        estq = get_object_or_404(Estoque, pk=pk)
        
        if 'quantidade' in data:
            prod = get_object_or_404(Produto, pk=estq.produto.pk)
            prod.quantidade -= estq.quantidade
            prod.quantidade += data['quantidade']
            prod.save()

        serializer.save()

class EstoqueVencidoView(generics.ListAPIView):
    queryset = Estoque.objects.filter(data_validade__lte = timezone.now())
    serializer_class = EstoqueDepthSerializer
    

class ProdutoView(generics.ListCreateAPIView):
    search_fields=['nome']
    filter_backends = (filters.SearchFilter,)
    queryset = Produto.objects.all().order_by('-id')
    serializer_class = ProdutoSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        time = timezone.now()
        data = self.request.data

        produto = serializer.save(data_insercao=time, desconto=0)

        preco = Preco(valor=data['preco_base'], data_alteracao=time, produto=produto)
        preco.save()

class ProdutoFaltaView(generics.ListAPIView):
    search_fields=['nome', 'descricao']
    filter_backends = (filters.SearchFilter,)
    queryset = Produto.objects.filter(quantidade__lte = F('quantidade_alerta')).order_by('-id')
    serializer_class = ProdutoSerializer
    pagination_class = CustomPagination


class ProdutoPartialView(generics.UpdateAPIView):

    def patch(self, request, pk):
        prod = get_object_or_404(Produto, pk=pk)
        serializer = ProdutoSerializer(prod, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save(pk=pk)
        return Response(serializer.data)


    def get(self, request, pk):
        prod = get_object_or_404(Produto, pk=pk)
        serializer = ProdutoSerializer(prod)
        return Response(serializer.data)
