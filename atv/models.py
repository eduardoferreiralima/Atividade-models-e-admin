
from django.db import models

# Create your models here.

class Products(models.Model):
    nome_produto = models.CharField(null=False, max_length=65)
    codigo_produto = models.CharField(primary_key=True, null=False, max_length=12)
    descricao = models.CharField(null=True, max_length=500)
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    quantidade_estoque = models.IntegerField()
    data_criacao = models.DateTimeField(auto_created=True)


'''Nome do produto (String, obrigatório).
Código do produto (String, único, obrigatório).
Descrição (Texto longo, opcional).
Preço (Decimal com 2 casas decimais).
Quantidade em estoque (Número inteiro).
Data de criação (Registrada automaticamente).'''