from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe

class Categoria(models.Model):
    categoria = models.CharField("categoria", max_length=200)


    def __str__(self):
        return self.categoria

class Opcoes(models.Model):
    nome = models.CharField("nome", max_length=100)
    acrecimo = models.FloatField("acrescimo", default=0)
    ativo = models.BooleanField("ativo", default=True)
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Opcoes" 
        verbose_name_plural = "Opcoes"

class Adicional(models.Model):
    nome = models.CharField("nome", max_length=100, unique=True)
    maximo = models.IntegerField()
    minimo = models.IntegerField()
    opcoes = models.ManyToManyField(Opcoes)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Adicional" 
        verbose_name_plural = "Adicionais"

class Produto(models.Model):
    nome_produto = models.CharField("nome", max_length=100)
    img = models.ImageField("imagem", upload_to='post_img')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.FloatField()
    descricao = models.TextField()
    ingredientes = models.CharField("ingredientes", max_length=2000)
    adicionais = models.ManyToManyField(Adicional, blank=True)
    ativo = models.BooleanField(default=True)

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="/media/{self.img}">'


    def __str__(self):
        return self.nome_produto
# Create your models here.
