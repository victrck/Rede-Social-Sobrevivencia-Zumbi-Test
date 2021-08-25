from sobrevivente.views import SinalizarContaminadoViewSet
from sobrevivente.views import SobreviventesListandCreate
from sobrevivente.views import ItemListandCreate
from sobrevivente.views import SobreviventeLocationUpdate
from django.urls import path

urlpatterns = [
    path('cadastrar/', SobreviventesListandCreate.as_view(), name='Sobrevivente'),
    path('item/', ItemListandCreate.as_view(), name='Item'),
    path('localizacao/',
         SobreviventeLocationUpdate.as_view({
             'put': 'update'
         }), name='localizacao'),
    path('sinalizarinfectado/',
         SinalizarContaminadoViewSet.as_view({
             'post': 'create'
         }), name='sinalizarinfectado'),
]
