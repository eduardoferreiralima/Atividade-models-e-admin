from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Products, Fornecedor, Categoria
from .forms import ProductsModelForm, FornecedorModelForm, CategoriaModelForm
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

def cadastrar_fornecedor(request):
    form = FornecedorModelForm(request.POST)
    print(request.POST)
    if request.method == "POST":
        categoria = Fornecedor(
            nome=request.POST.get("nome"),
            contato=request.POST.get("contato"),
            endereco=request.POST.get("endereco")
        )
        categoria.save()
    return render(request, 'atv/cadastrar_fornecedor.html', {'form':form})

def cadastrar_categoria(request):
    form = CategoriaModelForm(request.POST)
    print(request.POST)
    if request.method == "POST":
        categoria = Categoria(
            nome=request.POST.get("nome")
        )
        categoria.save()
    return render(request, 'atv/cadastrar_categoria.html', {'form':form})

def create(request):
    form = ProductsModelForm(request.POST or None)  # Inicializa o formulário com dados do request, se houver
    if request.method == "POST":
        if form.is_valid():  # Valida os dados do formulário
            # Coletar os dados do formulário
            nome = request.POST.get('nome')
            descricao = request.POST.get('descricao')
            codigo = request.POST.get('codigo')
            preco = request.POST.get('preco')
            quantidade_estoque = request.POST.get('quantidade_estoque')
            
            # Obter o fornecedor (ForeignKey)
            fornecedor = get_object_or_404(Fornecedor, id=request.POST.get('fornecedor'))
            
            # Obter as categorias (ManyToManyField)
            categorias_ids = request.POST.getlist('categorias')  # Lista de IDs de categorias
            categorias = Categoria.objects.filter(id__in=categorias_ids)  # Filtra as categorias existentes
            
            # Criar o objeto do produto
            produto = Products(
                nome=nome,
                descricao=descricao,
                preco=preco,
                codigo=codigo,
                quantidade_estoque=quantidade_estoque,
                fornecedor=fornecedor  # Associar o fornecedor ao produto
            )
            produto.save()  # Salva o produto no banco de dados
            
            # Associar as categorias ao produto
            produto.categorias.set(categorias)  # Define as categorias associadas
            produto.save()  # Salva novamente para garantir a associação
            
            # Redirecionar ou renderizar uma página de sucesso
        else:
            print("Erros no formulário:", form.errors)  # Depuração em caso de erro no formulário

    return render(request, 'atv/cadastrar_produto.html', {'form': form})