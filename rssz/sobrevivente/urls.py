from sobrevivente.views import SobreviventesListandCreate
from sobrevivente.views import ItemListandCreate
from django.urls import path

urlpatterns = [
    path('cadastrar/', SobreviventesListandCreate.as_view(), name='Sobrevivente'),
    path('item/', ItemListandCreate.as_view(), name='Item'),
]
