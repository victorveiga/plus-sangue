from django.db import models

# Create your models here.
class Doador(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    tipo_sanguineo = models.CharField(max_length=2)
    fator_rh = models.BooleanField()

    def __str__(self):
        return self.nome + ' - ' + self.sobrenome


