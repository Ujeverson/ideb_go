import pandas as pd
from django.shortcuts import render, redirect
from .models import Dados
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split




@login_required
def ia_import(request):
    if request.method == 'POST':
        arquivo = request.FILES.get('arquivo_csv')
        if not arquivo:
            messages.error(request, "Nenhum arquivo foi selecionado.")
            return redirect('insights:ia_import')

        if arquivo.name.endswith('.csv'):
            try:
                df = pd.read_csv(arquivo, sep=';', encoding='utf-8')
                # Salvar o arquivo no modelo
                Dados.objects.create(arquivo=arquivo)
                messages.success(request, "Arquivo CSV carregado com sucesso!")
                return redirect('insights:ia_import_list')
            except Exception as e:
                messages.error(request, f"Erro ao processar o arquivo: {e}")
        else:
            messages.error(request, "Formato de arquivo inválido. Apenas CSV é suportado.")
            return redirect('insights:ia_import')

    return render(request, 'insights/ia_import.html')

@login_required
def ia_import_list(request):
    data = {}
    data['dados'] = Dados.objects.all()
    return render(request, 'insights/ia_import_list.html', data)

@login_required
def visualizar_dados(request, pk):
    dado = Dados.objects.get(pk=pk)
    df = pd.read_csv(dado.arquivo.path, sep=';', encoding='utf-8')
    dados_html = df.to_html(classes='table table-striped', index=False)
    return render(request, 'insights/visualizar_dados.html', {'dados_html': dados_html})

@login_required
def treinar_knn(request, pk):
    dado = Dados.objects.get(pk=pk)
    df = pd.read_csv(dado.arquivo.path, sep=';', encoding='utf-8')

    # Filtrar colunas relevantes
    features = ['IDEB 2005', 'IDEB 2007', 'IDEB 2009', 'IDEB 2011', 'IDEB 2013', 'IDEB 2015', 'IDEB 2017', 'IDEB 2019']
    target = 'IDEB 2023'

    # Remover linhas com valores nulos
    df = df.dropna(subset=features + [target])

    X = df[features]
    y = df[target]

    # Dividir os dados
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinar o modelo
    model = KNeighborsRegressor(n_neighbors=3)
    model.fit(X_train, y_train)

    # Avaliar o modelo
    accuracy = model.score(X_test, y_test)

    return render(request, 'insights/treinar_knn.html', {'accuracy': accuracy})