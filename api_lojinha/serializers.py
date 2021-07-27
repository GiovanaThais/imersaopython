from rest_framework import serializers
from produto.models import Opcoes, Categoria, Adicional, Produto
#from pedido.models import Pedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields ='__all__'
    
class OpcoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcoes
        fields ='__all__'

class AdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adicional
        fields ='__all__'
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields ='__all__'
