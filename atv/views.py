from django.shortcuts import render, get_object_or_404
from .models import Products, Fornecedor, Categoria
# Create your views here.

def Lista_produtos(request):
    produtos = Products.objects.all()
    return render(request, 'atv/lista-produtos.html', {'produtos': produtos})

def Lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'atv/lista-produtos.html', {'categorias': categorias})

def Lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'atv/lista-produtos.html', {'fornecedores': fornecedores})

def Detalhes_produtos(request, codigo):
    produto = get_object_or_404(Products, codigo=codigo)
    return render(request, 'atv/detalhes-produto.html', {'produto': produto})