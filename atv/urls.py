from django.urls import path
from . import views

urlpatterns = [
    path('', views.Lista_produtos.as_view(), name='lista_produtos'),
    path('produtos/<str:codigo>/', views.Detalhes_produtos.as_view(), name='detalhes_produto'),
    path('cadastrar', views.create.as_view(), name="cadastrar_produto"),
    path('cadastrar-fornecedor/', views.cadastrar_fornecedor.as_view(), name="cadastrar_fornecedor"),
    path('cadastrar-categoria/', views.cadastrar_categoria.as_view(), name="cadastrar_categoria"),
]