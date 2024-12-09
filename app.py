import streamlit as st
import pickle
import matplotlib.pyplot as plt
import os
import time

#Configuração do layout da página no app.py
st.set_page_config(
    page_title="Dashboard do Clima de São Paulo vs. Buscas nas Internet",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Obter o caminho base do diretório onde o app.py está localizado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@st.cache_data
def load_graphics():
    graphics = {}
    file_paths = [
        "artefatos/meteorologico_tempo.pkl",
        "artefatos/sunrise_temperatura.pkl",
        "artefatos/sunrise_sunset.pkl",
        "artefatos/descricao_semanal.pkl",
        "artefatos/heatmap.pkl",
        "artefatos/pairplot.pkl",
        "artefatos/line_plot_nestle_marcas.pkl",
        "artefatos/line_plot_nestle.pkl",
        "artefatos/line_plot_saudavel.pkl",
    ]

    for path in file_paths:
        full_path = os.path.join(BASE_DIR, path)  # Caminho absoluto
        try:
            if os.path.exists(full_path):
                with open(full_path, "rb") as file:
                    filename = os.path.basename(path)  # Nome do arquivo
                    graphics[filename] = pickle.load(file)  # Usar nome do arquivo como chave
            else:
                st.warning(f"Arquivo {path} não encontrado.")
        except Exception as e:
            st.error(f"Erro ao carregar {path}: {e}")

    return graphics

graphics = load_graphics()

# Carregar o logo da Nestlé
logo_path = os.path.join(BASE_DIR, "artefatos/nestle_logo.png")  # Caminho absoluto

if os.path.exists(logo_path):
    st.image(logo_path, width=200)
else:
    st.error(f"Logo não encontrado: {logo_path}")


st.title("Dashboard do Clima de São Paulo vs. Buscas na Internet")

st.write("""
    Bem-vindo ao painel de visualização de dados do clima de São Paulo e busca por determinadas palavras no google nos últimos 2 anos. 
    
    No menu lateral, escolha um gráfico para visualização dos dados.
""")

# Seleção de gráficos
chart_type = st.sidebar.selectbox(
    'Escolha o gráfico',
    ['Home',
     'Heatmap de Correlações',
     'Pair Plot Clima e Buscas', 
     'Mais Análises do Clima São Paulo', ]
)

#Home Page
# Dados Meteorológicos ao longo do tempo
# Dados de Puscas ao longo do tempo
if chart_type == 'Home':
    # Adicionando notas
    st.markdown("""
    **Proposta:**
    A intenção desta breve investição é explorar a correlação entre variáveis de clima de São Paulo vs. buscas no google de interesse para a Nestlé.
    *Aqui temos apenas um piloto, que para uma aplicação prática precisamos ir muito mais além e fazer investigações mais robustas.

    _Neste exemplo, coletei dados das condições climáticas de São Paulo dos últimos 2 anos e buscas no Google por palavras como:_
    
    _**Nescafé, Dolce Gusto, Zero Açúcar, e Alimentação Saudável.**_
    
    **Fonte de Dados:**    
    - Os dados climático coletados foi utilizado da **API: Open Wethermap** (dados diários)
    - Os dados de palavras foi utilizado: o **Google Trends** (dados semanais)

    Sabemos que o clima e sasonalidade molda o comportamento humano. Mas como é o comportamento de busca das pessoas de acordo com as condições climáticas? Quanto é isso quantitativamente?
    Dados de eventos naturais alinhado com dados provindo de meios digitais pode nos dizer muito sobre o comportamento humano. Uma vez que essas duas fontes de informação estão nos impactando nosso inconsciente a todo momento.

    **Valor de Negócio:**
    - Auxiliar em decisões mais informadas em planejamento de marketing e definir ações de ativação em estações estratégicas para diferentes marcas;
    - Descobrir tendências de consumo com base no crescimento de determinado conceito;
    - Lançamento de produto em períodos mais estratégicos.
        
    _**Obs.: Evidentemente, para uma aplicação prática, precisamos de aprofundar nas pesquisas, fazer análises mais robustas e amadurecer a ideia.**_
    
    Em uma análise mais completa, podemos criar modelos que prevêm tendências de busca com base nos dados naturais, como sensação térmica e horário do pôr do sol, como as coletadas aqui.

    """)    
    
    st.subheader("Dados de Pesquisa de Palavras em São Paulo nos últimos 2 anos..")
    
    st.plotly_chart(graphics["line_plot_nestle_marcas.pkl"])  # Mostrar gráfico estático Matplotlib
    
    st.plotly_chart(graphics["line_plot_nestle.pkl"])  # Mostrar gráfico estático Matplotlib
        
    st.plotly_chart(graphics["line_plot_saudavel.pkl"])  # Mostrar gráfico estático Matplotlib   
    
    st.subheader("Dados Meteorológicos de SP ao longo de 2 anos")
    
    st.plotly_chart(graphics["meteorologico_tempo.pkl"])  # Mostrar gráfico estático Matplotlib
    
    st.text_area("Comentários sobre este gráfico:", "Adicione aqui suas observações sobre o gráfico de dados meteorológicos.")

  


# Heatmap de Correlação
elif chart_type == 'Heatmap de Correlações':
    st.subheader('Heatmap de Correlação')
    
    st.pyplot(graphics["heatmap.pkl"])
        
    # Adicionando notas
    st.markdown("""
    **Algumas Notas sobre o heatmap:**
    1) De acordom com a Alta Temperatura / Alta Sensação Térmica, temos:
    
    -- Palavras de alta busca no Google: 
    - Gelados : Sorvete, Gelado, Picolé, Frutas

    -- Palavras de média para alta busca no Google: 
    - Zero Açúcar : Pessoal tenta diminuir mais o açúcar em dias de alta temperatura
    - Supermercado: sugerindo uma pequena tendência para busca por supermercados em dias 
    - Comida integral

    -- Palavras com média busca no Google "Buscas para todas as temperaturas":
    - Sobremesa, Mousse, Barra de Cereal
    - Negresco
    - Passatempo
    - Calipso
    - Nestlé
    Vemos que certas palavras e certas marcas são para qualquer temperatura.

    -- Palavras de média para baixa busca no Google:
    - Nesfit, Galak

    -- Baixa procura: 
    - Nescafé, Dolce Gusto, Café, Café Solúvel, Cafeteira - Words Café
    - Bolo, Chocolate, Doce, Pizza - Words Não Saudáveis
    - Nescau
    - Molico

    - Chá - Sugerindo que chá ainda é muito relacionado com o frio, mesmo com as opções geladas
    - Receita : Indicando menos procura por termos 'receitas' em dias de sensação térmica maior
    - Cozinhar : Ao lado de receita, indica que a correlação entre temperatura e busca pelo termo cozinhar é negativa. Sugerindo que pessoas buscam por algo "cozinhar" menos em momentos de frio.


    2) Palavras:
    - Bolo e Chá estão altamente correlacionadas
    - Nescau e Receita estão altamente correlacionadas (como podemos ver pelo pair plot também)
    - E Quando a Busca por Receitas também aumentam, a busca por zero açúcar também diminui. É notável que existem certos momentos do ano em que comportamentos mudam e consequentemente a busca por determinados termos. Essa perspectiva merece uma análise mais profunda.

    Outra análise que pode ser explorada é com base na sazonalidade relacionada ao Sunset / Por do Sol:
        - Segue uma certa consistência período em que o por dol sol é mais tarde com períodos com maior temperatura.
        - Mas algumas correlações sofrem uma certa oscilação: como mousse e sobremesa são mais procuradas em períodos em que o por do sol se estende um pouco mais.
        
    """)
    
    st.text_area("Comentários sobre este gráfico:", "Adicione aqui suas observações..")


# Pair Plot de Correlação
elif chart_type == 'Pair Plot Clima e Buscas':
    st.subheader('Pair Plot de Correlações')
    
    st.pyplot(graphics["pairplot.pkl"])

    # Adicionando notas
    st.markdown("""
    **Notas sobre o Pair plot:**
    - As análises do pair plot vêm para confirmar as informações do heatmap e trazer uma visão mais detalhada do comportamento dos dados;
    - Os gráficos são exibidos com os pontos sendo distinguidos pela variável categórica "wether time"
    """)
    
    st.text_area("Comentários sobre este gráfico:", "Adicione aqui suas observações..")
    
    

# Relação entre Sunrise e Temperatura
elif chart_type == 'Mais Análises do Clima São Paulo':
    st.subheader('Desrição do tempo por semana nas últimas 105 semanas em São Paulo')
    st.plotly_chart(graphics["descricao_semanal.pkl"])  # Mostrar gráfico interativo Plotly
    st.text_area("Comentários sobre este gráfico 2:", "Adicione aqui suas observações..")
    
    
    st.subheader('Relação entre Sunrise e Temperatura')
    st.plotly_chart(graphics["sunrise_temperatura.pkl"])  # Mostrar gráfico interativo Plotly
    st.text_area("Comentários sobre este gráfico:", "Adicione aqui suas observações..")


    st.subheader('Nascer e Pôr do Sol em 2 anos')
    st.plotly_chart(graphics["sunrise_sunset.pkl"])  # Mostrar gráfico interativo Plotly
    st.text_area("Comentários sobre este gráfico 1:", "Adicione aqui suas observações..")
    

    

