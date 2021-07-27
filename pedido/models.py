from django.db import models
from datetime import datetime
from produto.models import Produto

class CupomDesconto(models.Model):
    codigo = models.CharField("codigo", max_length=8, unique=True)
    desconto = models.FloatField()
    usos = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.codigo
    

class Pedido(models.Model):
    usuario = models.CharField("usuario", max_length=200)
    total = models.FloatField()
    troco = models.CharField("troco", blank=True, max_length=20)
    cupom  = models.ForeignKey(CupomDesconto, null=True, blank=True, on_delete=models.CASCADE)
    pagamento = models.CharField("pagamento", max_length=20)
    ponto_referencia = models.CharField(max_length=2000, blank=True)
    data = models.DateTimeField("data", default=datetime.now())
    cep = models.CharField("cep", max_length=50, blank=True)
    rua = models.CharField("rua", max_length=200)
    numero = models.CharField("numero", max_length=10)
    bairro = models.CharField("bairro", max_length=200, blank=True)
    telefone = models.CharField("telefone", max_length=30)
    entregue = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    descricao = models.TextField()
    adicionais = models.TextField()
    
# Create your models here.

