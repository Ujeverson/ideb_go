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
    list_display = ('nome', 'email', 'celular', 'funcao', 'data_nascimento', 'idade', 'ativo')  # Adicionado 'idade'
    search_fields = ('nome', 'email', 'data_nascimento')
    list_filter = ('ativo', 'funcao')
    actions = [habilitar_pessoas, desabilitar_pessoas]

    def idade(self, obj):
        return obj.idade()  # Chama o método idade() do modelo
    idade.short_description = 'Idade'  # Nome da coluna no admin