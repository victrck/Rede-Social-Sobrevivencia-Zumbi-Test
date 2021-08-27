from sobrevivente.views import SinalizarContaminadoViewSet
from sobrevivente.views import SobreviventesListandCreate
from sobrevivente.views import ItemListandCreate, InventarioViewSet, SobreviventeLocationUpdate

from django.urls import path

urlpatterns = [
    path("cadastrar-sobrevivente/",
         SobreviventesListandCreate.as_view(), name="Sobrevivente"),
    path("cadastrar-item/", ItemListandCreate.as_view(), name="Item"),
    path("alterar-localizacao/",
         SobreviventeLocationUpdate.as_view({
             "put": "update"
         }), name="localizacao"),
    path("sinalizar-infectado/",
         SinalizarContaminadoViewSet.as_view({
             "post": "create"
         }), name="Sinalizar_infectado"),
    path("trocar-itens/",
         InventarioViewSet.as_view({
             "post": "create"
         }), name="Realizar_troca"),
]
