from django.db import models

# Create your models here.
class Doador(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    tipo_sanguineo = models.CharField(max_length=2)
    fator_rh = models.BooleanField()
    cpf = models.CharField(max_length = 11)
    rg = models.CharField(max_length = 10)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    fumante = models.BooleanField()
    peso = models.FloatField()
    altura = models.FloatField()
    sexo = models.BooleanField()
    nome_mae = models.CharField(max_length= 100)
    nome_pai = models.CharField(max_length= 100)
    profissao = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome + ' - ' + self.sobrenome


