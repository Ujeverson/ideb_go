from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Pessoa
from .forms import PessoaForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User


@login_required
def pessoa_list(request):
    # Verifica se o usuário é superusuário
    if not request.user.is_superuser:
        return render(request, 'people/permission_denied.html')  # Página de erro para permissão negada

    # Lista todos os usuários do sistema
    usuarios = User.objects.all()
    return render(request, 'people/pessoa_list.html', {'usuarios': usuarios})

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