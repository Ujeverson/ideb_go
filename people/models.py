from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    email = models.CharField(max_length=50, null=False, blank=False, verbose_name='eMail')
    celular = models.CharField(max_length=20, null=True, blank=True, verbose_name='Celular')
    funcao = models.CharField(max_length=30, null=True, blank=True, verbose_name='Função')
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self):
        return f'{self.nome} - {self.email}'

    def idade(self):
        if self.data_nascimento:
            hoje = date.today()
            idade = hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))
            return idade
        return None

    def clean(self):
        # Validação para garantir que a data de nascimento não seja no futuro
        if self.data_nascimento and self.data_nascimento > date.today():
            raise ValidationError({'data_nascimento': 'A data de nascimento não pode ser no futuro.'})

    