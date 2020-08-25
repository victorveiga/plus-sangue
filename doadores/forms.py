from django.forms import ModelForm, NumberInput, TextInput, Textarea, Select
from .models import Doador

class DoadorForm(ModelForm):
    class Meta:
        model  = Doador
        fields = ('nome', 'sobrenome', 'tipo_sanguineo', 'fator_rh', 'cpf', 'rg', 'idade', 'data_nascimento',
        'fumante', 'peso', 'altura', 'sexo', 'nome_mae', 'nome_pai', 'profissao')
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'tipo_sanguineo': 'Tipo Sanguíneo',
            'fator_rh': 'Fator RH',
            'cpf': 'CPF',
            'rg': 'RG',
            'idade': 'Idade',
            'data_nascimento': 'Data de nascimento',
            'fumante': 'Fumante?',
            'peso': 'Peso',
            'altura' : 'Altura',
            'sexo': 'Sexo',
            'nome_mae': 'Mãe',
            'nome_pai': 'Pai',
            'profissao': 'Profissão',
           
        }
        widgets = {
            'nome': TextInput(attrs={'placeholder': 'Informe o primeiro e real nome do herói'}),
            'sobrenome': TextInput(attrs={'placeholder': 'Agora, informe o sobrenome dele. Conte-nos esse segredo!'}),
            'tipo_sanguineo': Select(choices=(('', '--Selecione--'),('A','A'),('B', 'B'),('AB', 'AB'),('O','O'))),
            'fator_rh': Select(choices= (('', '--Selecione--'), (True, '+ (Positivo)'), (False, '- (Negativo)'))),
            'cpf': TextInput(attrs={'placeholder': 'Informe o seu CPF'}),
            'rg': TextInput(attrs={'placeholder': 'Informe o seu RG'}),
            'fumante': Select(choices=(('', '--Selecione--'), (True, 'Sim'), (False, 'Não'))),
            'peso': TextInput(attrs={'placeholder': 'Kg'}),
            'sexo': Select(choices=(('', '--Selecione--'), (True, 'Feminino'), (False, 'Masculino'))),
            'nome_mae': TextInput(attrs={'placeholder': 'Nome da mãe'}),
            'nome_pai': TextInput(attrs={'placeholder': 'Nome do pai'}),
            'profissao': TextInput(attrs={'placeholder': 'Informe sua profissão'}),

            
            

        }