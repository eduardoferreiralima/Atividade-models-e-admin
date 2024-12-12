
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=25)

class Fornecedor(models.Model):
    nome = models.CharField(max_length=35)
    endereco = models.CharField(max_length=50)
    contato = models.CharField(max_length=20)

class Products(models.Model):
    nome = models.CharField(null=False, max_length=65)
    codigo = models.CharField(primary_key=True, null=False, max_length=12)
    descricao = models.CharField(null=True, max_length=500)
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    quantidade_estoque = models.IntegerField()
    data_criacao = models.DateTimeField(auto_created=True)
    categorias = models.ManyToManyField(Categoria, related_name='produtos')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='produtos')
