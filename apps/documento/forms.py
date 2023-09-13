from django import forms
from .models import Documento

class DocumentoFilterForm(forms.Form):
    OPCOES = [
        ('True', 'Sim'),
        ('False', 'Não'),
    ]

    utiliza_num_ano = forms.CharField(
        label='Utiliza número e ano?',
        widget=forms.RadioSelect(
            choices=OPCOES
        ),
        initial="False"
    )

class DocumentoForm(forms.ModelForm):
    OPCOES = [
        ('True', 'Sim'),
        ('False', 'Não'),
    ]

    codigo = forms.IntegerField(
        label='Código',
        widget=forms.NumberInput(attrs={
            'type': 'number',
            'placeholder': 'Informe o código',
            'class': 'form-control col-md-4'
        }
        ))
    descricao = forms.CharField(
        label='Descrição',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Descrição",
                "class": "form-control col-md-8",
                "type": "text"
            }
        ))
    utiliza_num_ano = forms.CharField(
        label='Utiliza número e ano?',
        widget=forms.RadioSelect(
            choices=OPCOES
        ),
        initial="False"
    )

    class Meta:
        model = Documento
        fields = ('codigo', 'descricao', 'utiliza_num_ano')

