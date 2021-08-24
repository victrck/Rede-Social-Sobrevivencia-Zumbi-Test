from sobrevivente.models import Item
from sobrevivente.models import Sobrevivente
from sobrevivente.serializers import SobreviventeSerializer
from sobrevivente.serializers import ItemSerializer
from sobrevivente.utils import adicionar_inventario
from rest_framework import generics, status
from rest_framework.response import Response


class SobreviventesListandCreate(generics.ListCreateAPIView):
    serializer_class = SobreviventeSerializer
    queryset = Sobrevivente.objects.all()

    def create(self, request):
        inventario = self.request.data.get('inventario', None)
        dados_sobrevivente = {
            "nome": self.request.data.get("nome", None),
            "idade": self.request.data.get("idade", None),
            "sexo": self.request.data.get("sexo", None),
            "longitude": self.request.data.get("longitude", None),
            "latitude": self.request.data.get("longitude", None),
        }
        serializer_sobrevivente = SobreviventeSerializer(
            data=dados_sobrevivente)
        serializer_sobrevivente.is_valid(raise_exception=True)
        serializer_sobrevivente.save()
        # adicionar_inventario(dados_sobrevivente, inventario)
        return Response(
            data={"detalhes": "Sobrevivente Cadastrado com Sucesso"},
            status=status.HTTP_201_CREATED
        )


class ItemListandCreate(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
