from sobrevivente.models import Sobrevivente, Inventario, Item
from sobrevivente.serializers import SobreviventeSerializer

from rest_framework import status, viewsets
from rest_framework.response import Response


class InfectadosViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer

    def list(self, request):
        quantidade_sobreviventes = Sobrevivente.objects.count()
        quantidade_infectados = Sobrevivente.objects.filter(
            infectado=True).count()
        porcentagem = round(float(quantidade_infectados /
                            quantidade_sobreviventes) * 100, 2)
        porcentagem_string = str(porcentagem) + " %"

        response = {"sobreviventes_infectados": quantidade_infectados,
                    "porcentagem": porcentagem_string}

        return Response(data={"detalhes": response}, status=status.HTTP_200_OK)


class NaoInfectadosViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer

    def list(self, request):
        quantidade_sobreviventes = Sobrevivente.objects.count()
        quantidade_nao_infectados = Sobrevivente.objects.filter(
            infectado=False).count()
        porcentagem = round(
            float(quantidade_nao_infectados / quantidade_sobreviventes) * 100, 2)
        porcentagem = str(porcentagem) + " %"

        response = {"Sobreviventes_Nao_Infectados": quantidade_nao_infectados,
                    "Porcentagem": porcentagem}

        return Response(data={"detalhes": response}, status=status.HTTP_200_OK)


class RecursoporSobreviventeViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer

    def list(self, request):
        quantidade_sobreviventes = Sobrevivente.objects.filter(
            infectado=False).count()
        response = []
        for item in Item.objects.all():
            nome_item = item.nome
            quantidade_disponivel = 0

            inventario_item = Inventario.objects.filter(item=item)
            for inventario in inventario_item:
                if not inventario.sobrevivente.infectado:
                    quantidade_disponivel += inventario.quantidade

            media = round(float(quantidade_disponivel /
                          quantidade_sobreviventes), 2)

            media_sobrevivente = {
                "Item": nome_item, "Quantidade": quantidade_disponivel, "Media_por_Sobrevivente": media}
            response.append(media_sobrevivente)

        return Response(data={"detalhes": response}, status=status.HTTP_200_OK)


class PontosperdidosViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    queryset = Sobrevivente.objects.all()
    serializer_class = SobreviventeSerializer

    def list(self, request):

        quant_pontos_perdidos_total = 0
        pontos_perdidos_list = []
        infectados = Sobrevivente.objects.filter(infectado=True)

        for infectado in infectados:
            pontos_perdidos_infectado = 0
            recursos_do_infectado = Inventario.objects.filter(
                sobrevivente=infectado)
            for recurso in recursos_do_infectado:
                pontos_perdidos_infectado += (recurso.quantidade *
                                              recurso.item.pontos)

            quant_pontos_perdidos_total += pontos_perdidos_infectado
            pontos_perdidos_list.append(
                {"infectado": infectado.nome, "pontos_perdidos": pontos_perdidos_infectado})

        response = {"Total_Pontos_Perdidos": quant_pontos_perdidos_total,
                    "Detalhes": pontos_perdidos_list}
        return Response(data=response, status=status.HTTP_200_OK)
