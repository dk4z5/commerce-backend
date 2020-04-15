from django.db import models
from django.utils import timezone

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=120, blank=True)
    quantidade = models.IntegerField()
    quantidade_alerta = models.IntegerField('Quantidade Mínima para alerta')
    preco_base = models.FloatField('Preço da únidade')
    data_insercao = models.DateTimeField('Data de inserção do produto no banco de dados.')
    desconto = models.FloatField('Porcentagem de desconto')
    def __str__(self):
        return self.nome + ": Quantidade em Estoque " + str(self.quantidade)


class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    valido = models.BooleanField()
    data_validade = models.DateTimeField('Validade do produto.')
    data_chegada = models.DateTimeField('Data de chegada.')

    def __str__(self):
        return self.produto.nome + ' Quantidade: ' + str(self.quantidade) +' Validade: ' + str(self.data_validade) + " Data de chegada: " + str(self.data_chegada)

