from django.db import models

class Dados(models.Model):
    arquivo = models.FileField(upload_to='uploads/', null=True, blank=True)

    class Meta:
        permissions = [
            ("view_arquivos_enviados", "Can view Arquivos Enviados"),
            ("import_csv", "Can import CSV"),
            ("train_knn", "Can train KNN"),
        ]

    def __str__(self):
        if self.arquivo:
            return f"Arquivo: {self.arquivo.name}"
        return "Nenhum arquivo"