from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vinculo
from .forms import VinculoForm
from django.urls import reverse_lazy
from django.db.models import Q


class VinculoListView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      ListView):
    model = Vinculo
    paginate_by = 5
    context_object_name = 'vinculos'

    permission_required = ('vinculo.view_vinculo',)
    permission_denied_message = "Você não tem permissão para listar vínculos"


class VinculoCreateView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        CreateView):
    model = Vinculo
    form_class = VinculoForm
    context_object_name = 'vinculo'
    success_url = '/vinculo/'
    permission_required = ('vinculo.add_vinculo')
    permission_denied_message = "Você não tem permissão para cadastrar vínculos"


class VinculoUpdateView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        UpdateView):
    model = Vinculo
    form_class = VinculoForm
    context_object_name = 'vinculo'
    success_url = '/vinculo/'
    permission_required = ('vinculo.change_vinculo')
    permission_denied_message = "Você não tem permissão para atualizar vínculos"


class VinculoDeleteView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        DeleteView):
    model = Vinculo
    context_object_name = 'vinculo'
    success_url = reverse_lazy('vinculo_list')
    permission_required = ('vinculo.delete_vinculo')
    permission_denied_message = "Você não tem permissão para excluir vínculos"
