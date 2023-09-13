from django import forms
from .models import Interessado


class InteressadoForm(forms.ModelForm):

    nome = forms.CharField(
        label='Nome',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome ou razão social",
                "class": "form-control col-md-8",
                "type": "text"
            }
        ))

    nome_social = forms.CharField(
        label='Nome social',
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control col-md-8",
                "type": "text"
            }
        ))

    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control col-md-2'
            }
        )
    )

    cpf = forms.CharField(
        label='CPF',
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control col-md-4",
                "type": "text",
                'data-mask':"000.000.000-00",
                "id": "cpf"
            }
        ))

    cnpj = forms.CharField(
        label='CNPJ',
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control col-md-4",
                "type": "text",
                'data-mask':"00.000.000/0000-00",
                "id": "cnpj"
            }
    ))

    class Meta:
        model = Interessado
        fields = [
            'nome',
            'nome_social',
            'data_nascimento',
            'cpf',
            'cnpj',
        ]
