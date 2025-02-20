from django import forms
from .models import Fornecedor, Categoria, Products, CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
class ProductsModelForm(forms.ModelForm):
    codigo = forms.CharField(
        validators=[
            RegexValidator(
                regex="^[a-zA-Z0-9]+$",
                message="O código deve conter apenas letras e números (sem espaços ou caracteres especiais).",
                code="invalid_codigo"
            )
        ]
    )
    class Meta:
        model = Products
        fields = ['nome', 'descricao', 'imagem', 'codigo', 'preco', 'quantidade_estoque', 'fornecedor', 'categorias']
        labels = {'nome':'Nome do Produto', 
                  'descricao':'Descrição do Produto',
                  'imagem':'Imagem do Produto',
                  'codigo':'Código do Produto',
                  'preco':'Preço do Produto',
                  'quantidade_estoque':'Quantidade em Estoque',
                  'fornecedor':'Selecione o Fornecedor',
                  'categorias':'Selecione as Categorias'
                  }
    def clean_preco(self):
        preco = self.cleaned_data.get("preco")
        if preco <= 0:
            raise ValidationError("O preço do Produto deve ser maior que zero!")
        return preco
    
    def clean_quantidade_estoque(self):
        quantidade_estoque = self.cleaned_data.get("quantidade_estoque")
        if quantidade_estoque <= 0:
            raise ValidationError("A quantidade em estoque deve ser um número inteiro maior ou igual a zero!")
        return quantidade_estoque
    def clean_nome(self):
        nome = self.cleaned_data.get("nome")
        if len(nome) < 3:
            raise ValidationError("O nome do produto deve ter pelo menos 3 caracteres!")
        return nome
    


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

class CadastroModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        labels= {
            'first_name':'Primeiro Nome',
            'last_name':"Último nome",
            'username':'Nome de usuário',
            'email':'Endereço de E-mail',
            'password':'Senha'
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # 🔒 Criptografa a senha
        if commit:
            user.save()
        return user