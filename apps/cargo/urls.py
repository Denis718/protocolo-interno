from django.urls import path
from .views import *


urlpatterns = [
    path('', CargosListView.as_view(), name='cargo_list'),
    path('new/', CargoCreateView.as_view(), name='cargo_new'),
    path('edit/<pk>/', CargoUpdateView.as_view(), name='cargo_edit'),
    path('delete/<pk>/', CargoDeleteView.as_view(), name='cargo_delete')
]