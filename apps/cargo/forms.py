from django import forms
from .models import Cargo

class CargoForm(forms.ModelForm):
    nome = forms.CharField(
        label='Cargo',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome do cargo",
                "class": "form-control col-md-8",
                "type": "text"
            }
        )
    )
    classe = forms.CharField(
        label='Classe',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Classe",
                "class": "form-control col-md-8",
                "type": "text"
            }
        )
    )
    jornada = forms.IntegerField(
        label='Jornada',
        widget=forms.NumberInput(
            attrs={
                "type": "number",
                "placeholder": "Jornada de trabalho",
                "class": "form-control col-md-3"
            }
        )
    )

    class Meta:
        model = Cargo
        fields = ('nome', 'classe', 'jornada')