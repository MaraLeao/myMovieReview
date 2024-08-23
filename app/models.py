from django.db import models

# Create your models here.

class Endereco(models.Model):
    cep = models.IntegerField()
    logradouro = models.CharField(blank=True, null=True, max_length=200)
    bairro = models.CharField(blank=True, null=True, max_length=200)
    localidade = models.CharField(blank=True, null=True, max_length=200)
    uf = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return (f'Aqui está os dados requisitados {self.cep}, {self.logradouro}, {self.bairro}, {self.localidade} - {self.uf}')
