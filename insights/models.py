# insights/models.py
from django.db import models

class Dados(models.Model):
    arquivo = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        if self.arquivo:
            return f"Arquivo: {self.arquivo.name}"
        return "Nenhum arquivo"