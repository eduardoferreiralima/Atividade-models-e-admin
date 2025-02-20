
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, default=None, null=True, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    


class Categoria(models.Model):
    nome = models.CharField(max_length=25)
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=35)
    endereco = models.CharField(max_length=50)
    contato = models.CharField(max_length=20)
    def __str__(self):
        return self.nome

class Products(models.Model):
    nome = models.CharField(null=False, max_length=65)
    codigo = models.CharField(primary_key=True, max_length=12)
    descricao = models.CharField(null=True, max_length=500)
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    quantidade_estoque = models.IntegerField()
    data_criacao = models.DateTimeField(auto_created=True, auto_now=True)
    categorias = models.ManyToManyField(Categoria, related_name='produtos')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='produtos')
    imagem = models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None, default=None, null=True)

    def __str__(self):
        return self.nome


