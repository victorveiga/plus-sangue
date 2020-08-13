from django.forms import ModelForm, NumberInput, TextInput, Textarea
from .models import Hemonucleo

class HemonucleoForm(ModelForm):
    class Meta:
        model  = Hemonucleo
        fields = ('nome', 'endereco')
        labels = {
            'nome': 'Nome',
            'endereco': 'Endereço',
        }
        widgets = {
            'nome': TextInput(attrs={'placeholder': 'Informe o nome de identificação da instituição.'}),
            'endereco': TextInput(attrs={'placeholder': 'Escreva o endereço do Hemonúcleo.'}),
        }