from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Lista_produtos.as_view(), name='lista_produtos'),
    path('produtos/<str:codigo>/', views.Detalhes_produtos.as_view(), name='detalhes_produto'),
    path('cadastrar', views.create.as_view(), name="cadastrar_produto"),
    path('cadastrar-fornecedor/', views.cadastrar_fornecedor.as_view(), name="cadastrar_fornecedor"),
    path('cadastrar-categoria/', views.cadastrar_categoria.as_view(), name="cadastrar_categoria"),
    path('login', views.login.as_view(), name="login"),
    path('logout', views.logout_view, name="logout"),
    path('cadastro', views.cadastro.as_view(), name="cadastro"),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
