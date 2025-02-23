# ideb_insights

![Django Version](https://img.shields.io/badge/Django-4.x-brightgreen)
![Python Version](https://img.shields.io/badge/Python-3.x-blue)

## Descrição

O **ideb_go** é uma aplicação web desenvolvida em Django que permite carregar dados (CSV/XLSX), manipulá-los usando Python, treinar modelos de Machine Learning (LLM) e visualizar os resultados em uma interface amigável. O projeto utiliza tecnologias como Bootstrap para o design responsivo e Plotly para gráficos interativos.

### Funcionalidades Principais

- **Carregamento de Dados**: Importe arquivos CSV ou Excel para análise.
- **Manipulação de Dados**: Use Python para processar e transformar os dados.
- **Treinamento de Modelos**: Treine modelos de Machine Learning (ex.: KNN) usando scikit-learn.
- **Visualização de Resultados**: Exiba gráficos, matriz de confusão, curvas ROC e Recall.
- **Autenticação**: Sistema de login/logout com permissões granulares.
- **Interface Responsiva**: Design moderno baseado no template [Bootstrap Blog](https://getbootstrap.com.br/docs/4.1/examples/blog/).

### Estrutura do Projeto

- **`insights`**: App principal para carregar, processar e visualizar dados.
- **`admin`**: Interface administrativa personalizada com CRUD e tabelas dinâmicas.
- **`core`**: App para funcionalidades compartilhadas, como autenticação e templates base.
- **`ia`**: App dedicada ao treinamento de modelos de IA e visualização dos resultados.

### Tecnologias Utilizadas

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Banco de Dados**: SQLite (padrão), PostgreSQL (opcional)
- **Machine Learning**: scikit-learn, Plotly, joblib
- **API de IA**: Groq API com modelo Gemma2-9B-IT

### Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ideb_insights.git
   cd ideb_insights
2. Crie e ative um ambiente virtual:
    ```bash
        python -m venv venv
        # No Windows:
        venv\Scripts\activate
        # No Linux/Mac:
        source venv/bin/activate
    ```

3. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
4. Execute as migrações do banco de dados:
    ````
    python manage.py migrate
    ````

5. Crie um superusuário:
    ````
    python manage.py createsuperuser
    ````
6. Inicie o servidor de desenvolvimento:
    ````
    python manage.py runserver
    ````
7. Acesse a aplicação em http://127.0.0.1:8000/.
   
### Contribuições
Contribuições são bem-vindas! Siga as diretrizes abaixo:

Faça um fork do repositório.

Crie uma branch para sua feature (````git checkout -b feature/nome-da-feature````).

Faça commit das suas alterações (````git commit -m 'Adiciona nova feature'````).

Envie para o repositório remoto (````git push origin feature/nome-da-feature````).

Abra um Pull Request.

#### Licença
Este projeto está licenciado sob a MIT License . Consulte o arquivo LICENSE para mais detalhes. 
  