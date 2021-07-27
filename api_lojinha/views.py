from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.serializers import Serializer
from api_lojinha import serializers
from rest_framework.generics import get_object_or_404
from produto import models
#from pedido import models
from .serializers import OpcoesSerializer,CategoriaSerializer,ProdutoSerializer,AdicionalSerializer

class ListarOpcoesViewSet(generics.ListCreateAPIView):
    serializer_class =OpcoesSerializer
    queryset = models.Opcoes.objects.all()

class OpcoesAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OpcoesSerializer
    queryset = models.Opcoes.objects.all()

class ListarProdutoAPIView(generics.ListCreateAPIView):
    serializer_class = ProdutoSerializer
    queryset = models.Produto.objects.all()

class ProdutoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProdutoSerializer
    queryset = models.Produto.objects.all()
    

class ListarCategoriaAPIView(generics.ListCreateAPIView):
    serializer_class = CategoriaSerializer
    queryset = models.Categoria.objects.all()

class CategoriaAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoriaSerializer
    queryset = models.Categoria.objects.all()

class ListarAdicionaisAPIView(generics.ListCreateAPIView):
    serializer_class = AdicionalSerializer
    queryset = models.Adicional.objects.all()

class AdicionalAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdicionalSerializer
    queryset = models.Adicional.objects.all()

#class PedidoAPIView(generics.ListCreateAPIView):
    #serializer_class = PedidoSerializer
    #queryset = models.Pedido.objects.all()

#class ItemPedidoAPIView(generics.RetrieveUpdateDestroyAPIView):
    #serializer_class = ItemPedidoSerializer
    #queryset = models.ItemPedido.objects.all()
    #def get_queryset(self):
        #if self.kwargs.get('pedido_pk'):
            #return self.queryset.filter(pedido_id=self.kwargs.get('pedido_pk'))
        #return self.queryset.all()
# Create your views here.
