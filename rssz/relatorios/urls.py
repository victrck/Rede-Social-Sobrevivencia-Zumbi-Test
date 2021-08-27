from django.urls import path
from relatorios.views import InfectadosViewSet, NaoInfectadosViewSet, RecursoporSobreviventeViewSet, PontosperdidosViewSet

urlpatterns = [

    path("infectados/", InfectadosViewSet.as_view({
        "get": "list"
    }), name="sobreviventes-infectados"),

    path("nao-infectados/", NaoInfectadosViewSet.as_view({
        "get": "list"
    }), name="nao-infectados"),

    path("recurso-sobrevivente/", RecursoporSobreviventeViewSet.as_view({
        "get": "list"
    }), name="recurso-por-sobrevivente"),

    path("pontos-perdidos/", PontosperdidosViewSet.as_view({
        "get": "list"
    }), name="pontos-perdidos")

]
