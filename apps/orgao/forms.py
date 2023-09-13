from django import forms
from .models import Orgao


class OrgaoForm(forms.ModelForm):
    TIPO_UNIDADE = [
        ('F', 'Formal'),
        ('I', 'Informal')
    ]

    SITUACAO_UNIDADE = [
        ('A', 'Ativa'),
        ('I', 'Inativa')
    ]

    nome = forms.CharField(
        label='Órgão',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome do orgão",
                "class": "form-control",
                "type": "text",
                "id": "inputNome"
            }
        )
    )
    sigla = forms.CharField(
        label='Sigla',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sigla",
                "class": "form-control",
                "type": "text",
                "id": "inputSigla"
            }
        )
    )
    tipo = forms.ChoiceField(
        label='Tipo',
        choices=TIPO_UNIDADE,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "inputTipo"
            }
        )
    )
    situacao = forms.ChoiceField(
        label='Situação',
        choices=SITUACAO_UNIDADE,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "inputSituacao"
            }
        )
    )

    class Meta:
        model = Orgao
        fields = ('nome', 'sigla', 'tipo', 'situacao')
