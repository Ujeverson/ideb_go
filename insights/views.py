import pandas as pd
from django.shortcuts import render, redirect
from .models import Dados
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns



def prever_ideb(request):
    # Carregar os dados mais recentes do banco de dados
    dados_obj = Dados.objects.last()  # Último arquivo enviado
    if not dados_obj:
        return redirect('insights:ia_import')  # Redirecionar se não houver dados

    # Ler o arquivo salvo
    df = pd.read_csv(dados_obj.arquivo.path, sep=';', encoding='utf-8')

    # Preparar os dados
    X_train, X_test, y_train, y_test = preparar_dados(df)

    # Treinar o modelo
    modelo, y_pred = treinar_knn(X_train, X_test, y_train, y_test)

    # Criar um DataFrame com os resultados
    resultados = pd.DataFrame({
        'Valores Reais': y_test,
        'Valores Previstos': y_pred
    })

    # Converter para formato JSON para exibir no template
    resultados_json = resultados.to_dict(orient='records')

    # Renderizar a página com os resultados
    return render(request, 'insights/previsoes.html', {'resultados': resultados_json})


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


def ia_import_list(request):
    data = {}
    data['dados'] = Dados.objects.all()
    return render(request, 'insights/ia_import_list.html', data)


def visualizar_dados(request, pk):
    dado = Dados.objects.get(pk=pk)
    df = pd.read_csv(dado.arquivo.path, sep=';', encoding='utf-8')
    dados_html = df.to_html(classes='table table-striped', index=False)
    return render(request, 'insights/visualizar_dados.html', {'dados_html': dados_html})


def treinar_knn(X_train, X_test, y_train, y_test):
    # Criar e treinar o modelo KNN
    knn = KNeighborsRegressor(n_neighbors=5)
    knn.fit(X_train, y_train)
    
    # Fazer previsões
    y_pred = knn.predict(X_test)
    
    # Avaliar o modelo
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"MSE: {mse:.2f}")
    print(f"R²: {r2:.2f}")
    
    return knn, y_pred


def grafico_view(request):
    # Exemplo de dados para o gráfico
    dados = {
        'labels': ['2005', '2007', '2009', '2011', '2013', '2015', '2017', '2019', '2023'],
        'valores': [3.4, 3.6, 3.8, 4.0, 4.2, 4.5, 4.7, 4.9, 5.1],
    }
    return render(request, 'insights/grafico.html', {'dados': dados})


def ia_import(request):
    if request.method == 'POST':
        arquivo = request.FILES.get('arquivo_csv')
        if not arquivo:
            return redirect('insights:ia_import')

        # Ler o arquivo
        if arquivo.name.endswith('.csv'):
            df = pd.read_csv(arquivo, sep=';', encoding='utf-8')
        elif arquivo.name.endswith('.xlsx'):
            df = pd.read_excel(arquivo)
        else:
            return redirect('insights:ia_import')

        # Salvar o arquivo no banco de dados
        Dados.objects.create(arquivo=arquivo)

        # Redirecionar para a página de lista de arquivos
        return redirect('insights:ia_import_list')
    
    return render(request, 'insights/ia_import.html')



def preparar_dados(df):
    # Selecionar apenas as colunas de IDEB
    ideb_columns = [col for col in df.columns if 'IDEB' in col]
    
    if not ideb_columns:
        raise ValueError("O arquivo carregado não contém colunas com 'IDEB'. Verifique o formato do arquivo.")
    
    # Features: Todos os anos exceto o último (2023)
    X = df[ideb_columns[:-1]].fillna(0)
    
    # Labels: Último ano (2023)
    y = df[ideb_columns[-1]].fillna(0)
    
    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Padronizar os dados
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test


def plotar_resultados(y_test, y_pred):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred, color='blue', label='Valores Previstos')
    sns.lineplot(x=[y_test.min(), y_test.max()], y=[y_test.min(), y_test.max()], color='red', label='Linha Ideal')
    plt.title('Comparação entre Valores Reais e Previstos')
    plt.xlabel('Valores Reais')
    plt.ylabel('Valores Previstos')
    plt.legend()
    plt.show()
    
    

def plotar_evolucao_ideb(df, escola_nome):
    escola = df[df['Nome da Escola'] == escola_nome]
    if escola.empty:
        print("Escola não encontrada.")
        return
    
    ideb_columns = [col for col in df.columns if 'IDEB' in col]
    anos = [int(col.split()[1]) for col in ideb_columns]  # Extrair os anos
    valores = escola[ideb_columns].values.flatten()  # Pegar os valores do IDEB
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=anos, y=valores, marker='o', color='green')
    plt.title(f'Evolução do IDEB - {escola_nome}')
    plt.xlabel('Ano')
    plt.ylabel('IDEB')
    plt.grid(True)
    plt.show()
    



def treinar_knn_view(df):
    # Carregar o último arquivo enviado
    dados_obj = Dados.objects.last()
    if not dados_obj:
        messages.error(request, "Nenhum arquivo disponível para treinamento.")
        return redirect('insights:ia_import')

    # Ler o arquivo salvo
    df = pd.read_csv(dados_obj.arquivo.path, sep=';', encoding='utf-8')
    
    # Debug: Imprimir colunas do DataFrame
    print("Colunas do DataFrame:", df.columns)
    
    # Preparar os dados
    try:
        X_train, X_test, y_train, y_test = preparar_dados(df)
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('insights:ia_import')

    # Treinar o modelo KNN
    knn = KNeighborsRegressor(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    # Avaliar o modelo
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Salvar os resultados no contexto
    resultados = {
        'mse': mse,
        'r2': r2,
        'y_test': y_test.tolist(),
        'y_pred': y_pred.tolist(),
    }

    # Renderizar a página com os resultados
    return render(df, 'insights/treinar_knn.html', {'resultados': resultados})