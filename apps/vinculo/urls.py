from django.urls import path
from .views import *


urlpatterns = [
    path('', VinculoListView.as_view(), name='vinculo_list'),
    path('novo/', VinculoCreateView.as_view(), name='vinculo_novo'),
    path('editar/<pk>/', VinculoUpdateView.as_view(), name='vinculo_editar'),
    path('delete/<pk>/', VinculoDeleteView.as_view(), name='vinculo_excluir')
]
