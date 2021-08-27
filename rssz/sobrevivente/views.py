from sobrevivente.serializers import InventarioSerializer, SobreviventeSerializer, ItemSerializer, SinalizarContaminadoSerializer
from sobrevivente.models import Item, Sobrevivente, Inventario, SinalizarContaminado

from rest_framework import generics, status, viewsets
from rest_framework.response import Response


class SobreviventesListandCreate(generics.ListCreateAPIView):

    serializer_class = SobreviventeSerializer
    queryset = Sobrevivente.objects.all()

    def create(self, request):
        try:
            novo_sobrevivente = Sobrevivente.objects.create(nome=self.request.data.get("nome", None), idade=self.request.data.get(
                "idade", None), sexo=self.request.data.get("sexo", None), latitude=self.request.data.get("latitude", None), longitude=self.request.data.get("longitude", None))
        except:
            return Response(data={"Detalhes": "Error! Sobrevivente com dados faltando!"}, status=status.HTTP_400_BAD_REQUEST)

        inventario = self.request.data.get("inventario", None)
        if inventario != None:
            for i in inventario:
                item = Item.objects.get(nome=i["item"])
                Inventario.objects.create(
                    quantidade=i["quantidade"], item=item, sobrevivente=novo_sobrevivente)

        return Response(data={"Detalhes": "Sobrevivente Cadastrado com Sucesso"}, status=status.HTTP_201_CREATED)


class ItemListandCreate(generics.ListCreateAPIView):

    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def create(self, request):
        try:
            item_data = {"nome": self.request.data.get(
                "nome", None), "pontos": self.request.data.get("pontos", None), }
            serializer_item = ItemSerializer(data=item_data)
            serializer_item.is_valid(raise_exception=True)
            serializer_item.save()
            return Response(data={"Detalhes": "Item Cadastrado com Sucesso"}, status=status.HTTP_201_CREATED)
        except:
            return Response(data={"Detalhes": "Error! Item com dados faltando ou já cadastrado."}, status=status.HTTP_400_BAD_REQUEST)


class SobreviventeLocationUpdate(viewsets.ModelViewSet):
    http_method_names = ["put"]
    serializer_class = SobreviventeSerializer
    queryset = Sobrevivente.objects.all()

    def update(self, request):
        try:
            sobrevivente = Sobrevivente.objects.get(
                id=self.request.data.get("id_sobrevivente", None))
            serializer_sobrevivente = SobreviventeSerializer(
                sobrevivente, data=request.data, partial=True)
            serializer_sobrevivente.is_valid(raise_exception=True)
            serializer_sobrevivente.save()
            return Response(data={"Detalhes": "Atualização de localização realizada."}, status=status.HTTP_200_OK)
        except:
            return Response(data={"Detalhes": "Sobrevivente não encontrado!"}, status=status.HTTP_400_BAD_REQUEST)


class SinalizarContaminadoViewSet(viewsets.ModelViewSet):
    http_method_names = ["post"]
    serializer_class = SinalizarContaminadoSerializer
    queryset = SinalizarContaminado.objects.all()

    def create(self, request):

        try:
            if self.request.data.get("sinalizado_por", None) == self.request.data.get("possivel_infectado", None):
                return Response(data={"Detalhes": "Verifique os campos informados."}, status=status.HTTP_400_BAD_REQUEST)
            sobrevivente_sinaliza = Sobrevivente.objects.get(
                id=self.request.data.get("sinalizado_por", None), infectado=False)
        except:
            return Response(
                data={"Detalhes": " O sobrevivente que está sinalizando não existe ou está infectado. "}, status=status.HTTP_400_BAD_REQUEST)
        verificar_quant_relatos = SinalizarContaminado.objects.filter(
            possivel_infectado=self.request.data.get("possivel_infectado", None)).count()
        if verificar_quant_relatos < 3:
            possivel_infectado = Sobrevivente.objects.get(
                id=self.request.data.get("possivel_infectado", None), infectado=False)
            SinalizarContaminado.objects.create(
                sinalizado_por=sobrevivente_sinaliza,
                possivel_infectado=possivel_infectado,
            )

            verificar_quant_relatos = SinalizarContaminado.objects.filter(
                possivel_infectado=self.request.data.get("possivel_infectado", None)).count()
            if verificar_quant_relatos >= 3:
                serializer_sobrevivente = SobreviventeSerializer(
                    possivel_infectado, data={"infectado": True, }, partial=True)
                serializer_sobrevivente.is_valid(raise_exception=True)
                serializer_sobrevivente.save()
                return Response(
                    data={"Detalhes": "Sinalização de Infecção de sobrevivente realizada com sucesso!"}, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    data={"Detalhes": "Sinalização de Infecção de sobrevivente realizada com sucesso!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"Detalhes": "Sobrevivente ja infectado."}, status=status.HTTP_400_BAD_REQUEST)


class InventarioViewSet(viewsets.ModelViewSet):

    http_method_names = ["post"]
    serializer_class = InventarioSerializer

    def create(self, request):
        try:
            id_sobrevivente1 = self.request.data["sobrevivente1"]["id_sobrevivente"]
            id_sobrevivente2 = self.request.data["sobrevivente2"]["id_sobrevivente"]
            if id_sobrevivente1 == id_sobrevivente2:
                return Response(data={"Detalhes": "A troca não pode ser feita por 2 sobreviventes iguais."}, status=status.HTTP_400_BAD_REQUEST)
            sobrevivente1 = Sobrevivente.objects.get(
                id=id_sobrevivente1, infectado=False)
            sobrevivente2 = Sobrevivente.objects.get(
                id=id_sobrevivente2, infectado=False)
            itens_troca_sobrevivente1 = self.request.data["sobrevivente1"]["inventario"]
            itens_troca_sobrevivente2 = self.request.data["sobrevivente2"]["inventario"]
            pontos_sobrevivente1 = 0
            pontos_sobrevivente2 = 0

            for i in itens_troca_sobrevivente1:
                nome_item = i["item"]
                quantidade_item = i["quantidade"]
                item = Item.objects.get(nome=nome_item)
                pontos_sobrevivente1 = pontos_sobrevivente1 + \
                    (item.pontos * quantidade_item)
                inventario_sobrevivente1 = Inventario.objects.get(
                    item=item, sobrevivente=sobrevivente1)
                if inventario_sobrevivente1 == None or inventario_sobrevivente1.quantidade < quantidade_item:
                    return Response(data={"detalhes": "Sobrevivente1: Não Possui Recursos Suficientes para a Troca."}, status=status.HTTP_400_BAD_REQUEST)

            for x in itens_troca_sobrevivente2:
                nome_item = x["item"]
                quantidade_item = x["quantidade"]
                item = Item.objects.get(nome=nome_item)
                pontos_sobrevivente2 = pontos_sobrevivente2 + \
                    (item.pontos * quantidade_item)
                inventario_sobrevivente2 = Inventario.objects.get(
                    item=item, sobrevivente=sobrevivente2)
                if inventario_sobrevivente2 == None or inventario_sobrevivente2.quantidade < quantidade_item:
                    return Response(data={"detalhes": "Sobrevivente2: Não Possui Recursos Suficientes para a Troca."}, status=status.HTTP_400_BAD_REQUEST)

            if pontos_sobrevivente1 == pontos_sobrevivente2:
                for i in itens_troca_sobrevivente2:
                    item = Item.objects.get(nome=i["item"])
                    try:
                        inventario_sobrevivente1 = Inventario.objects.get(
                            item=item, sobrevivente=sobrevivente1)
                    except:
                        inventario_sobrevivente1 = None
                    if inventario_sobrevivente1 != None:
                        inventario_sobrevivente1.quantidade += i["quantidade"]
                        inventario_sobrevivente1.save()
                    else:
                        novo_inventario = Inventario.objects.create(
                            item=item, quantidade=i["quantidade"], sobrevivente=sobrevivente1)
                        novo_inventario.save()

                for i in itens_troca_sobrevivente1:
                    item = Item.objects.get(nome=i["item"])
                    try:
                        inventario_sobrevivente1 = Inventario.objects.get(
                            item=item, sobrevivente=sobrevivente1)
                    except:
                        inventario_sobrevivente1 = None
                    if inventario_sobrevivente1 != None:
                        inventario_sobrevivente1.quantidade -= i["quantidade"]
                        inventario_sobrevivente1.save()

                for i in itens_troca_sobrevivente1:
                    item = Item.objects.get(nome=i["item"])
                    try:
                        inventario_sobrevivente2 = Inventario.objects.get(
                            item=item, sobrevivente=sobrevivente2)
                    except:
                        inventario_sobrevivente2 = None
                    if inventario_sobrevivente2 != None:
                        inventario_sobrevivente2.quantidade += i["quantidade"]
                        inventario_sobrevivente2.save()
                    else:
                        novo_inventario = Inventario.objects.create(
                            item=item, quantidade=i["quantidade"], sobrevivente=sobrevivente2)
                        novo_inventario.save()

                for i in itens_troca_sobrevivente2:
                    item = Item.objects.get(nome=i["item"])
                    try:
                        inventario_sobrevivente2 = Inventario.objects.get(
                            item=item, sobrevivente=sobrevivente2)
                    except:
                        inventario_sobrevivente2 = None
                    if inventario_sobrevivente2 != None:
                        inventario_sobrevivente2.quantidade -= i["quantidade"]
                        inventario_sobrevivente2.save()
                return Response(data={"detalhes": "Troca Realizada com Sucesso."}, status=status.HTTP_200_OK)
        except:
            return Response(data={"Detalhes": "Dados incompletos ou faltando. Verifique os dados informados."}, status=status.HTTP_400_BAD_REQUEST)
