from re import A
from django.urls import path
from . import views

from api_lojinha.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categoria', ListarCategoriaAPIView, CategoriaAPIView)
router.register('opcoes', ListarOpcoesViewSet, OpcoesAPIView)
router.register('adicional', ListarAdicionaisAPIView, AdicionalAPIView)

urlpatterns = [
    path("", views.home, name='home'),
    path("categoria/<int:id>", views.categorias, name='categoria'),
    path("categorias/", ListarCategoriaAPIView.as_view(), name='categorias'),
    path("categorias/<int:pk>/", CategoriaAPIView.as_view(), name='categoria_api'),
    path("opcoes/", ListarOpcoesViewSet.as_view(), name='opcoes'),
    path("opcoes/<int:pk>/", OpcoesAPIView.as_view(), name='opcoes_api'),
    path("adicionais/", ListarAdicionaisAPIView.as_view(), name='adicional'),
    path("adicional/<int:pk>/", AdicionalAPIView.as_view(), name='adicional_api'),
    path("produto/<int:id>", views.produto, name='produto'),
    path("add_carrinho", views.add_carrinho, name='add_carrinho'),
    path("ver_carrinho", views.ver_carrinho, name='ver_carrinho'),
    path("remover_carrinho/<int:id>", views.remover_carrinho, name='remover_carrinho'),
]