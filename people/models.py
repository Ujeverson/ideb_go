from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    email = models.CharField(max_length=50, null=False, blank=False, verbose_name='eMail')
    celular = models.CharField(max_length=20, null=True, blank=True, verbose_name='celular')
    funcao = models.CharField(max_length=30, null=True, blank=True, verbose_name='Funcao')
    # Opcional: Caso queira armazenar data de nascimento e idade:
    # data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    # idade = models.IntegerField(null=True, blank=True, verbose_name='Idade')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self):
        return f'{self.nome} - {self.email}'
