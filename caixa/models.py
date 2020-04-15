from django.db import models

# Create your models here.
from estoque.models import Produto

class Venda(models.Model):
    MODOS_COMPRA = [ 
        ('debit', 'debit'),
        ('credit', 'credit'),
        ('money', 'money'),
        ('nesp', 'nesp')
    ]

    data = models.DateTimeField('Data da venda')
    cliente = models.CharField(max_length=60)
    preco_total = models.FloatField('Preço total') # novo
    desconto = models.FloatField('Desconto Total')
    pagamento = models.CharField(max_length=6,choices=MODOS_COMPRA, default='nesp')
    recebido = models.FloatField('Dinheiro recebido')
    
class RetiradaProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    venda = models.ForeignKey(Venda, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    desconto = models.FloatField("Desconto no produto.")

    def save(self):
        prod = self.produto
        models.Model.save(self)

        prod.quantidade -= self.quantidade
        prod.save()



class Preco(models.Model):
    valor = models.FloatField("Valor do produto")
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    data_alteracao = models.DateTimeField('Data da alteração')
    
""" class Balanco(models.Model):
    data_emissao = models.DateTimeField("Data de realização")
    data_inicio = models.DateField("Data Inicio")
    data_fim = models.DateField("Data Fim")
    
    
class BalancoCaixa(models.Model):
    data_emissao = models.DateTimeField("Data de realização")
    valor = models.IntegerField("Dinheiro em caixa") """