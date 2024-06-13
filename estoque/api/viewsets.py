from rest_framework import viewsets
from estoque.api import serializers
from estoque import models

class RelogioCorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RelogioCorSerializer
    queryset = models.RelogioCor.objects.all()

class MarcaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MarcaSerializer
    queryset = models.Marca.objects.all()

class RelogioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RelogioSerializer
    queryset = models.Relogio.objects.all()

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()

class VendedorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VendedorSerializer
    queryset = models.Vendedor.objects.all()

class VendaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VendaSerializer
    queryset = models.Venda.objects.all()

class ControleVendaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ControleVendaSerializer
    queryset = models.ControleVenda.objects.all()

class EstoqueViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EstoqueSerializer
    queryset = models.Estoque.objects.all()