from django.shortcuts import render
from .models import Orgao
from .forms import OrgaoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import QuerySet

class OrgaoListView(LoginRequiredMixin,
                    PermissionRequiredMixin,
                    ListView):
    model = Orgao
    paginate_by = 5
    context_object_name = 'orgaos'
    permission_required = ('orgao.view_orgao',)
    permission_denied_message = "Você não tem permissão para listar Orgãos."


class OrgaoCreateView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      CreateView):
    model = Orgao
    form_class = OrgaoForm
    context_object_name = 'orgao'
    success_url = '/orgao/'
    permission_required = ('orgao.add_orgao',)
    permission_denied_message = "Você não tem permissão para criar  orgãos."

class OrgaoUpdateView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      UpdateView):
    model = Orgao
    form_class = OrgaoForm
    context_object_name = 'orgao'
    success_url = '/orgao/'
    permission_required = ('orgao.add_orgao',)
    permission_denied_message = "Você não tem permissão para atualiar orgãos."

class OrgaoDeleteView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      DeleteView):
    model = Orgao
    context_object_name = 'orgao'
    success_url = reverse_lazy('orgaos_lista')
    permission_required = ('orgao.delete_orgao',)
    permission_denied_message = "Você não tem permissão para excluir órgãos."