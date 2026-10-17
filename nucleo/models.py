from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    telefone = models.CharField(max_length=30)
    setor = models.ForeignKey("nucleo.Setor", verbose_name='Setor', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nome

class Setor(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.nome
