import os
import joblib
import pandas as pd
import numpy as np
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from .models import Dados


@login_required
def upload_csv_view(request):
    return render(request, 'insights/upload_csv.html')


@login_required
def ia_import(request):
    if request.method == 'POST':
        arquivo = request.FILES.get('arquivo_csv')
        if not arquivo:
            messages.error(request, "Nenhum arquivo foi selecionado.")
            return redirect('insights:ia_import')

        if arquivo.name.endswith('.csv'):
            df = pd.read_csv(arquivo)
        elif arquivo.name.endswith('.xlsx'):
            df = pd.read_excel(arquivo)
        else:
            messages.error(request, "Formato de arquivo inválido.")
            return redirect('insights:ia_import')

        # Salvar o arquivo no modelo
        dados_obj = Dados.objects.create(arquivo=arquivo)
        messages.success(request, "Dados importados com sucesso!")
        return redirect('insights:ia_import_list')
    
    return render(request, 'insights/ia_import.html')

@login_required
def ia_import_list(request):
    data = {}
    data['dados'] = Dados.objects.all()
    return render(request, 'insights/ia_import_list.html', data)



@login_required
@permission_required('insights.view_arquivos_enviados', raise_exception=True)
def ia_import_list(request):
    data = {}
    data['dados'] = Dados.objects.all()
    return render(request, 'insights/ia_import_list.html', data)