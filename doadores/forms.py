from django.forms import ModelForm, NumberInput, TextInput, Textarea
from .models import Doador

class DoadorForm(ModelForm):
    class Meta:
        model  = Doador
        fields = ('nome', 'sobrenome', 'tipo_sanguineo')
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'tipo_sanguineo': 'Tipo Sanguíneo',
        }
        widgets = {
            'nome': TextInput(attrs={'placeholder': 'Informe o primeiro e real nome do herói'}),
            'sobrenome': TextInput(attrs={'placeholder': 'Agora, informe o sobrenome dele. Conte-nos esse segredo!'}),
            'tipo_sanguineo': TextInput(attrs={'placeholder': 'O tipo sanguíneo, isso é muito importante!'}),
        }