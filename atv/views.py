from .models import Products, Fornecedor, Categoria,CustomUser
from .forms import ProductsModelForm, FornecedorModelForm, CategoriaModelForm,CadastroModelForm
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
# Create your views here.

class Lista_produtos(LoginRequiredMixin, ListView):
    model = Products
    template_name = 'atv/lista-produtos.html'
    context_object_name = 'produtos'
    paginate_by = 5

    def get_queryset(self):
        busca = self.request.GET.get('busca')
        preco_min = self.request.GET.get('preco_min')
        preco_max = self.request.GET.get('preco_max')
        queryset = Products.objects.all()
        for produto in queryset: print(produto.imagem)

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

class Detalhes_produtos(LoginRequiredMixin, DetailView):
    model = Products
    template_name = "atv/detalhes-produto.html"  # Template para exibição dos detalhes
    context_object_name = "produto"  # Variável que será usada no template
    slug_field = "codigo"  # Campo do modelo usado para busca
    slug_url_kwarg = "codigo"  # Nome do parâmetro na URL

class cadastrar_fornecedor(LoginRequiredMixin, CreateView):
    model = Fornecedor
    form_class = FornecedorModelForm
    template_name = 'atv/cadastrar_fornecedor.html'
    success_url = reverse_lazy('cadastrar_produto')


class cadastrar_categoria(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaModelForm
    template_name = 'atv/cadastrar_categoria.html'
    success_url = reverse_lazy('cadastrar_produto')
    
class create(LoginRequiredMixin, CreateView):
    model = Products
    form_class = ProductsModelForm
    template_name = 'atv/cadastrar_produto.html'
    success_url = reverse_lazy('cadastrar_produto') 
    def form_valid(self, form):
        messages.success(self.request, "Produto cadastrado com sucesso!")
        return super().form_valid(form)
    
class cadastro(CreateView):
    model=CustomUser
    form_class=CadastroModelForm
    template_name='atv/cadastro.html'
    success_url = reverse_lazy('login')

class login(LoginView):
    
    redirect_authenticated_user=True
    success_url = 'lista_produtos'
    template_name = 'atv/login.html'


def logout_view(request):
   logout(request)
   return redirect('login')
