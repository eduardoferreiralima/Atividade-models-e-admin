from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.Lista_produtos, name='lista_produtos'),
    path('produtos/<str:codigo>/', views.Detalhes_produtos, name='detalhes_produto'),
    path('categorias/', views.Lista_categorias, name='lista_categorias'),
    path('fornecedores/', views.Lista_fornecedores, name='lista_fornecedores'),
]