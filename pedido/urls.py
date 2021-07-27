from django.urls import path
from . import views
from api_lojinha.views_pedido import PedidoAPIView, ItemPedidoAPIView
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('pedidos', PedidoAPIView)
router.register('item', ItemPedidoAPIView)
urlpatterns = [
    path("finalizar_pedido/", views.finalizar_pedido, name='finalizar_pedido'),
    path("validaCupom/", views.validaCupom, name='validaCupom'),
    path("pedidos_api/", PedidoAPIView.as_view(), name='pedido_api'),
    path("pedidos_api/<int:pk>/", ItemPedidoAPIView.as_view(), name='pedidos_api')
]