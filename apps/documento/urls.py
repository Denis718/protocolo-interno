from django.urls import path
from .views import *


urlpatterns = [
    path('', DocumentosListView.as_view(), name='document_list'),
    path('novo/', DocumentoCreateView.as_view(), name='document_new'),
    path('<pk>/edit/', DocumentoUpdateView.as_view(), name='document_edit'),
    path('delete/<pk>/', DocumentoDeleteView.as_view(), name='document_delete'),
]