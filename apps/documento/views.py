from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import DocumentoForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Documento
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator
from django.urls import reverse_lazy



class DocumentosListView(LoginRequiredMixin, 
                         PermissionRequiredMixin, 
                         ListView):
    model = Documento
    paginate_by = 5
    context_object_name = 'documentos'

    permission_required = ('documento.view_documento',)
    permission_denied_message = "Você não tem permissão para listar documentos"

    # Search bar query
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(descricao__icontains=search))
        return queryset

# @login_required(login_url="/login/")
# def document_list(request):
    
#     search_document = request.GET.get('search')

#     if search_document:
#         documents = Documento.objects.filter(Q(descricao__icontains=search_document))
#     else:
#         # If not searched, return default documents
#         documents = Documento.objects.all().order_by('codigo')

#     paginator=Paginator(documents, 5)  # Show 5 documents per page.
#     page_number=request.GET.get("page")
#     page_obj=paginator.get_page(page_number)

#     context={"page_obj": page_obj}
#     return render(request, "documento/documento.html", context)
    # return HttpResponse(form.as_p())

class DocumentoCreateView(LoginRequiredMixin,
                          PermissionRequiredMixin,
                          CreateView):

    model = Documento
    form_class = DocumentoForm
    context_object_name = 'documento'
    success_url = '/documento/'
    permission_required = ('documento.add_documento', )
    permission_denied_message = "Você não tem permissão para cadastrar documentos"
    
    def form_valid(self, form):
        # recupera o formulário enviado no post, antes do commit
        documento = form.save(commit=False)
        # insere o usuario informado no request
        documento.createdBy = self.request.user
        # Salva o model documento
        documento.save()
        # retornar o formulário válido para a superclasse
        return super(DocumentoCreateView, self).form_valid(form)


# @ login_required(login_url="/login/")
# def document_new(request):
#     form=DocumentoForm(request.POST or None)
#     form.fields['utiliza_num_ano'].initial="False"

#     msg=None

#     if request.method == "POST":

#         if form.is_valid():
#             document=form.save(commit=False)
#             document.createdBy=request.user
#             document.save()

#             return redirect('document_list')
#         else:
#             msg='Error validating the form'

#     return render(request, "documento/documento-edit.html", {"form": form, "msg": msg})


class DocumentoUpdateView(LoginRequiredMixin,
                          PermissionRequiredMixin,
                          UpdateView):
    model = Documento
    form_class = DocumentoForm
    context_object_name = 'documento'
    success_url = '/documento/'
    permission_required = ('documento.change_documento', )
    permission_denied_message = "Você não tem permissão para editar documentos"

    def form_valid(self, form):
        documento=form.save(commit=False)
        documento.modifyBy= self.request.user
        documento.modifyAt=timezone.now()
        documento.save()

        return super(DocumentoUpdateView, self).form_valid(form)

# @ login_required(login_url="/login/")
# def document_edit(request, pk):
#     document=get_object_or_404(Documento, pk=pk)
#     if request.method == "POST":
#         form=DocumentoForm(request.POST, instance=document)
#         if form.is_valid():
#             document=form.save(commit=False)
#             document.modifyBy=request.user
#             document.modifyAt=timezone.now()
#             document.save()
#             return redirect('document_list')
#     else:
#         form=DocumentoForm(instance=document)
#     return render(request, 'documento/documento_form.html', {'form': form})


class DocumentoDeleteView(LoginRequiredMixin,
                          PermissionRequiredMixin,
                          DeleteView):
    model = Documento
    context_object_name = 'documento'
    success_url = reverse_lazy('document_list')
    permission_required = ('documento.delete_documento')
    permission_denied_message = "Você não tem permissão para excluir documentos"

# def document_delete(request, pk):
#     Documento.objects.filter(pk=pk).delete()

#     return redirect('document_list')
