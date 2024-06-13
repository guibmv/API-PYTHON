from rest_framework import serializers
from estoque import models

class RelogioCorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RelogioCor
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'

class RelogioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Relogio
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendedor
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Venda
        fields = '__all__'

class ControleVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ControleVenda
        fields = '__all__'

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estoque
        fields = '__all__'