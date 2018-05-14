from django.db import models

# Create your models here.

class Troxa(models.Model):
    primeiro_nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.primeiro_nome} {self.sobrenome}'