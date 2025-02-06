from encodings import search_function
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Products, Fornecedor, Categoria
from .forms import ProductsModelForm, FornecedorModelForm, CategoriaModelForm
from django.views.generic import ListView, CreateView, DetailView
from django.db.models import Q
from django.urls import reverse_lazy
# Create your views here.

class Lista_produtos(ListView):
    model = Products
    template_name = 'atv/lista-produtos.html'
    context_object_name = 'produtos'
    paginate_by = 5

    def get_queryset(self):
        busca = self.request.GET.get('busca')
        preco_min = self.request.GET.get('preco_min')
        preco_max = self.request.GET.get('preco_max')
        queryset = Products.objects.all()

        if preco_min:
            print('preco')
            queryset = queryset.filter(preco__gte=preco_min)

        if preco_max:
            print('preco')
            queryset = queryset.filter(preco__lte=preco_max)

        if preco_max and preco_min:
            print('preco')
            queryset = queryset.filter(Q(preco__gte=preco_min) & Q(preco__lte=preco_max))

        if busca:
            queryset = queryset.filter(nome__icontains=busca)
        return queryset

class Detalhes_produtos(DetailView):
    model = Products
    template_name = "atv/detalhes-produto.html"  # Template para exibição dos detalhes
    context_object_name = "produto"  # Variável que será usada no template
    slug_field = "codigo"  # Campo do modelo usado para busca
    slug_url_kwarg = "codigo"  # Nome do parâmetro na URL

class cadastrar_fornecedor(CreateView):
    model = Fornecedor
    form_class = FornecedorModelForm
    template_name = 'atv/cadastrar_fornecedor.html'
    success_url = reverse_lazy('cadastrar_produto')


class cadastrar_categoria(CreateView):
    model = Categoria
    form_class = CategoriaModelForm
    template_name = 'atv/cadastrar_categoria.html'
    success_url = reverse_lazy('cadastrar_produto')
    

class create(CreateView):
    model = Products
    form_class = ProductsModelForm
    template_name = 'atv/cadastrar_produto.html'
    success_url = reverse_lazy('lista_produtos') 