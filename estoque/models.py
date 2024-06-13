from django.db import models
from uuid import uuid4

# Create your models here.


class RelogioCor(models.Model):
    IdCor = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Color = models.CharField(max_length=50)

class Marca(models.Model):
    IdMarca = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    Marca = models.CharField(max_length=50)

class Relogio(models.Model):
    IdRelogio = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    IdMarca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    IdCor = models.ForeignKey(RelogioCor, on_delete=models.CASCADE)
    Preco = models.IntegerField()
    Garantia = models.CharField(max_length=30)
    Referencia = models.CharField(max_length=30)

class Cliente(models.Model):
    IdCliente = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    NomeCliente = models.CharField(max_length=255)
    TelefoneCliente = models.IntegerField()

class Vendedor(models.Model):
    IdVendedor = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    NomeVendedor = models.CharField(max_length=255)
    TelefoneVendedor = models.BigIntegerField()

class Venda(models.Model):
    IdVenda = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    IdCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    IdVendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    MetodoPag = models.CharField(max_length=50)
    Parcelas = models.IntegerField()
    DataVenda = models.DateField(auto_now_add=True)

class ControleVenda(models.Model):
    IdControleVenda = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    IdRelogio = models.ForeignKey(Relogio, on_delete=models.CASCADE)
    IdVenda = models.ForeignKey(Venda, on_delete=models.CASCADE)

class Estoque(models.Model):
    IdEstoque = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    IdRelogio = models.ForeignKey(Relogio, on_delete=models.CASCADE)
    Quantidade = models.IntegerField()
    DataAtualizacao = models.DateField(auto_now_add=True)    