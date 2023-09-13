from django.urls import path
from .views import (OrgaoListView,
                    OrgaoCreateView,
                    OrgaoUpdateView,
                    OrgaoDeleteView
                    )

urlpatterns = [
    path('', OrgaoListView.as_view(), name='orgaos_lista'),
    path('novo/', OrgaoCreateView.as_view(), name='orgao_novo'),
    path('editar/<pk>/', OrgaoUpdateView.as_view(), name='orgao_editar'),
    path('delete/<pk>/', OrgaoDeleteView.as_view(), name='orgao_excluir'),
]
