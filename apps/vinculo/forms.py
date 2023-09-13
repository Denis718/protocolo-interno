from django import forms
import apps
from apps.cargo.models import Cargo
from mptt.forms import TreeNodeChoiceField
from apps.orgao.models import Orgao
from account.models import CustomUser
from .models import Vinculo


class VinculoForm(forms.ModelForm):
    servidor = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    matricula = forms.IntegerField(
        label='Matrícula',
        widget=forms.NumberInput(
            attrs={
                "type": "number",
                "placeholder": "999999",
                "class": "form-control"
            }
        )
    )

    lotacao = TreeNodeChoiceField(
        queryset=Orgao.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    data_inicio = forms.DateField(
        label='Data de início',
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control"
            }
        )
    )

    data_fim = forms.DateField(
        label='Data de término',
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "disabled": "true",
                "id": "dtfim",
            }
        ),
        required=False
    )
    cargo = forms.ModelChoiceField(
        queryset=Cargo.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    situacao = forms.BooleanField(
        # label='Situação',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "type": "checkbox",
                "class": "custom-control-input",
                "id": "customSwitch1",
                "onclick": "status_dtfim()"
            }
        )
    )
    class Meta:
        model = Vinculo
        fields = ('servidor', 'matricula', 'lotacao',
                  'data_inicio', 'data_fim', 'cargo', 'situacao')
