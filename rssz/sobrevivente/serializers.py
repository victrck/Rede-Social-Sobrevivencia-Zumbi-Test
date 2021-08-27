from sobrevivente.models import Sobrevivente, Item, Inventario, SinalizarContaminado

from rest_framework import serializers


class SobreviventeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = "__all__"


class SinalizarContaminadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinalizarContaminado
        fields = "__all__"
