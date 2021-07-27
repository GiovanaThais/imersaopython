from rest_framework import generics
from rest_framework.serializers import Serializer
from pedido import models
from .serializers_pedido import PedidoSerializer, ItemPedidoSerializer

class PedidoAPIView(generics.ListCreateAPIView):
    serializer_class = PedidoSerializer
    queryset = models.Pedido.objects.all()

class ItemPedidoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemPedidoSerializer
    queryset = models.ItemPedido.objects.all()
    
