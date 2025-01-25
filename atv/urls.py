from django.urls import path
from . import views

urlpatterns = [
    path('', views.Lista_produtos, name='lista_produtos'),
    path('produtos/<str:codigo>/', views.Detalhes_produtos, name='detalhes_produto'),
    path('categorias/', views.Lista_categorias, name='lista_categorias'),
    path('fornecedores/', views.Lista_fornecedores, name='lista_fornecedores'),
    path('cadastrar', views.create, name="cadastrar_produto"),
    path('cadastrar-fornecedor/', views.cadastrar_fornecedor, name="cadastrar_fornecedor"),
    path('cadastrar-categoria/', views.cadastrar_categoria, name="cadastrar_categoria"),
]