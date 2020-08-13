from django.db import models

# Create your models here.
class Hemonucleo(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
