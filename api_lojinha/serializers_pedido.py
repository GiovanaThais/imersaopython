from rest_framework import serializers
from pedido.models import Pedido, ItemPedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields ='__all__'

class  ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields ='__all__'

