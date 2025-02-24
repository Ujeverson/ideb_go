from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Pessoa
from .forms import PessoaForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User


@login_required
def pessoa_list(request):
    pessoas = Pessoa.objects.all()
    for pessoa in pessoas:
        pessoa.idade_calculada = pessoa.idade()  # Calcula a idade para cada pessoa
    return render(request, 'people/pessoa_list.html', {'pessoas': pessoas})

def pessoa_create(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pessoa criada com sucesso!")
            return redirect('people:pessoa_list')
    else:
        form = PessoaForm()
    return render(request, 'people/pessoa_form.html', {'form': form})

def pessoa_update(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            messages.success(request, "Pessoa atualizada com sucesso!")
            return redirect('people:pessoa_list')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'people/pessoa_form.html', {'form': form})

def pessoa_delete(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        messages.success(request, "Pessoa excluída com sucesso!")
        return redirect('people:pessoa_list')
    return render(request, 'people/pessoa_confirm_delete.html', {'pessoa': pessoa})