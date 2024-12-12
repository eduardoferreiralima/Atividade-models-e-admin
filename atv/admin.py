from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Products, Categoria, Fornecedor



@admin.register(Products)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'preco', 'quantidade_estoque', 'data_criacao')  # Campos na listagem
    search_fields = ('codigo', 'nome')  # Campos para busca
    list_filter = ('data_criacao',)  # Filtro por data de criação
    ordering = ('-data_criacao',)  # Ordenação decrescente

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato')
    search_fields = ('nome',)
