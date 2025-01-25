from django import forms
from .models import Fornecedor, Categoria, Products
class ProductsModelForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['nome', 'descricao', 'codigo', 'preco', 'quantidade_estoque', 'fornecedor', 'categorias']
        labels = {'nome':'Nome do Produto', 
                  'descricao':'Descrição do Produto',
                  'codigo':'Código do Produto',
                  'preco':'Preço do Produto',
                  'quantidade_estoque':'Quantidade em Estoque',
                  'fornecedor':'Selecione o Fornecedor',
                  'categorias':'Selecione as Categorias'
                  }

class FornecedorModelForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome','endereco','contato']
        labels = {
            'nome':'Nome do Fornecedor',
            'endereco':'Endereço',
            'contato':'Contato'
        }

class CategoriaModelForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {
            'nome':'Nome da Categoria'
        }