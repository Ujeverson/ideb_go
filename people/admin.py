from django.contrib import admin
from .models import Pessoa

@admin.action(description='Habilitar pessoas selecionadas')
def habilitar_pessoas(modeladmin, request, queryset):
    queryset.update(ativo=True)

@admin.action(description='Desabilitar pessoas selecionadas')
def desabilitar_pessoas(modeladmin, request, queryset):
    queryset.update(ativo=False)

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'celular', 'funcao', 'ativo')
    search_fields = ('nome', 'email')
    list_filter = ('ativo', 'funcao')
    actions = [habilitar_pessoas, desabilitar_pessoas]
