from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cargo
from .forms import CargoForm
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

class CargosListView(LoginRequiredMixin,
                     PermissionRequiredMixin,
                     ListView):
    model = Cargo
    paginate_by = 5
    context_object_name = 'cargos'

    permission_required = ('cargo.view_cargo',)
    permission_denied_message = "Você não tem permissão para listar cargos"

    # Search bar query
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(nome__icontains=search))
        return queryset



class CargoCreateView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      CreateView):
    model = Cargo
    form_class = CargoForm
    context_object_name = 'cargo'
    success_url = '/cargo/'
    permission_required = ('cargo.add_cargo')
    permission_denied_message = "Você não tem permissão para cadastrar cargos"


class CargoUpdateView(LoginRequiredMixin,
                    PermissionRequiredMixin,
                    UpdateView,):
    model = Cargo
    form_class = CargoForm
    context_object_name = 'cargo'
    success_url = '/cargo/'
    permission_required = ('cargo.change_cargo')
    permission_denied_message = "Você não tem permissão para editar cargos"


class CargoDeleteView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      DeleteView):
    model = Cargo
    context_object_name = 'cargo'
    success_url = reverse_lazy('cargo_list')
    permission_required = ('cargo.delete_cargo')
    permission_denied_message = "Você não tem permissão para excluir cargos"