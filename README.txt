projeto_nestle/
│
├── .streamlit/                       # Configurações específicas do Streamlit
│   └── config.toml                   # Arquivo de configuração do Streamlit
│
├── artefatos/                         # Plots gerados e outros artefatos
│   ├── descricao_semanal.pkl          # Dados de descrição semanal
│   ├── heatmap.pkl                    # Arquivo de dados para gráfico de heatmap
│   ├── meteorologico_tempo.pkl        # Dados de gráfico meteorológico de tempo
│   ├── nestle_logo.png                # Logo da Nestlé
│   ├── pairplot.pkl                   # Dados para o gráfico Pairplot
│   ├── sunrise_sunset.pkl             # Dados de nascer e pôr do sol
│   └── sunrise_temperatura.pkl        # Dados de temperatura ao nascer do sol
│
├── google_trends/                     # Dados de tendências do Google
│   ├── multiTimeline_cafe.csv         # Dados de tendências de busca para café
│   ├── multiTimeline_diversos.csv     # Dados de tendências de busca para diversos temas
│   ├── multiTimeline_gelados.csv      # Dados de tendências de busca para gelados
│   ├── multiTimeline_n_saudavel.csv  # Dados de tendências de busca para "não saudável"
│   ├── multiTimeline_nestle_marcas.csv # Dados de tendências de busca para marcas da Nestlé
│   ├── multiTimeline_nestle_nescau.csv # Dados de tendências de busca para Nestlé Nescau
│   └── multiTimeline_nestle_saude.csv  # Dados de tendências de busca para saúde da Nestlé
│
├── outros_arquivos_csv/               # Arquivos CSV adicionais
│   ├── dados_climaticos_semanais_sp.csv  # Dados climáticos semanais de São Paulo
│   ├── historico_temperatura_umidade_sao_paulo_2.csv # Dados históricos de temperatura e umidade de São Paulo (2)
│   ├── historico_temperatura_umidade_sao_paulo_3.csv # Dados históricos de temperatura e umidade de São Paulo (3)
│
├── app.py                             # Arquivo principal da aplicação Streamlit
└── requirements.txt                   # Arquivo com as dependências do projeto