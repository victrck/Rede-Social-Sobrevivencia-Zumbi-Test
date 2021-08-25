from sobrevivente.models import Item, Sobrevivente, Inventario, SinalizarContaminado
from sobrevivente.serializers import SobreviventeSerializer
from sobrevivente.serializers import ItemSerializer
from sobrevivente.serializers import SinalizarContaminadoSerializer
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class SobreviventesListandCreate(generics.ListCreateAPIView):
    '''
    Cadastrar um novo Sobrevivente.
    '''

    serializer_class = SobreviventeSerializer
    queryset = Sobrevivente.objects.all()

    def create(self, request):
        try:
            sobrevivente = {
                "nome": self.request.data.get("nome", None),
                "idade": self.request.data.get("idade", None),
                "sexo": self.request.data.get("sexo", None),
                "longitude": self.request.data.get("longitude", None),
                "latitude": self.request.data.get("latitude", None),
            }
            serializer_sobrevivente = SobreviventeSerializer(data=sobrevivente)
            serializer_sobrevivente.is_valid(raise_exception=True)
            serializer_sobrevivente.save()
        except:
            return Response(
                data={"Detalhes": "Error! Sobrevivente com dados faltando!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            inventario = self.request.data.get('inventario', None)
            for i in inventario:
                item = Item.objects.get(nome=i['item'])
                Inventario.objects.create(
                    quantidade=i['quantidade'], item=item, sobrevivente=sobrevivente)
        except:
            pass

        return Response(
            data={"Detalhes": "Sobrevivente Cadastrado com Sucesso"},
            status=status.HTTP_201_CREATED
        )


class ItemListandCreate(generics.ListCreateAPIView):
    '''
    Cadastrar um novo Item.
    '''

    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def create(self, request):
        try:
            item_data = {
                "nome": self.request.data.get("nome", None),
                "pontos": self.request.data.get("pontos", None),
            }
            serializer_item = ItemSerializer(data=item_data)
            serializer_item.is_valid(raise_exception=True)
            serializer_item.save()
            return Response(
                data={"Detalhes": "Item Cadastrado com Sucesso"},
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                data={"Detalhes": "Error! Item com dados faltando!"},
                status=status.HTTP_400_BAD_REQUEST
            )


class SobreviventeLocationUpdate(viewsets.ModelViewSet):
    http_method_names = ['put']
    serializer_class = SobreviventeSerializer
    queryset = Sobrevivente.objects.all()

    def update(self, request):
        try:
            sobrevivente = Sobrevivente.objects.get(
                id=self.request.data.get('id_sobrevivente', None))
            serializer_sobrevivente = SobreviventeSerializer(
                sobrevivente, data=request.data, partial=True)
            serializer_sobrevivente.is_valid(raise_exception=True)
            serializer_sobrevivente.save()
            return Response(
                data={"Detalhes": "Atualização de localização realizada."},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                data={"Detalhes": "Sobrevivente não encontrado!"},
                status=status.HTTP_400_BAD_REQUEST
            )


class SinalizarContaminadoViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    serializer_class = SinalizarContaminadoSerializer
    queryset = SinalizarContaminado.objects.all()

    def create(self, request):

        try:
            if self.request.data.get('sinalizado_por', None) == self.request.data.get('possivel_infectado', None):
                return Response(
                    data={"Detalhes": "Verifique os campos informados."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            sobrevivente_sinaliza = Sobrevivente.objects.get(
                id=self.request.data.get('sinalizado_por', None), infectado=False)
        except:
            return Response(
                data={
                    "Detalhes": " O sobrevivente que está sinalizando não existe ou está infectado. "},
                status=status.HTTP_400_BAD_REQUEST
            )
        verificar_quant_relatos = SinalizarContaminado.objects.filter(
            possivel_infectado=self.request.data.get('possivel_infectado', None)).count()
        if verificar_quant_relatos < 3:
            possivel_infectado = Sobrevivente.objects.get(
                id=self.request.data.get('possivel_infectado', None), infectado=False)
            SinalizarContaminado.objects.create(
                sinalizado_por=sobrevivente_sinaliza,
                possivel_infectado=possivel_infectado,
            )

            verificar_quant_relatos = SinalizarContaminado.objects.filter(
                possivel_infectado=self.request.data.get('possivel_infectado', None)).count()
            if verificar_quant_relatos >= 3:
                serializer_sobrevivente = SobreviventeSerializer(
                    possivel_infectado, data={"infectado": True, }, partial=True)
                serializer_sobrevivente.is_valid(raise_exception=True)
                serializer_sobrevivente.save()
                return Response(
                    data={
                        "Detalhes": "Sinalização de Infecção de sobrevivente realizada com sucesso!"},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    data={
                        "Detalhes": "Sinalização de Infecção de sobrevivente realizada com sucesso!"},
                    status=status.HTTP_201_CREATED
                )
        else:
            return Response(
                data={"Detalhes": "Sobrevivente ja infectado."},
                status=status.HTTP_400_BAD_REQUEST
            )
