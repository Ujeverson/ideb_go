from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from people.models import Pessoa

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Pessoa.objects.create(user=instance)

@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    if hasattr(instance, 'pessoa'):
        instance.pessoa.save()