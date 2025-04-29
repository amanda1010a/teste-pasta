import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import timedelta

st.write("""
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações brasileiras ao longo dos anos
""")

@st.cache_data
def carregar_dados(empresas):
    dados_acao = yf.Tickers(empresas)
    precos_acao = dados_acao.history(period='1d', start='2015-01-01', end='2024-07-01')
    precos_acao = precos_acao["Close"]
    return precos_acao

dados  = carregar_dados("ITUB4.SA BBAS3.SA VALE3.SA ABEV3.SA MGLU3.SA PETR4.SA GGBR4.SA")

barra_lateral = st.sidebar.header("Filtros")
lista_acoes = st.sidebar.multiselect("Escolha as ações para exibir no gráfico", dados.columns)
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_datas = st.sidebar.slider("Selecione o período", 
                                    min_value=data_inicial, 
                                    max_value=data_final, value=(data_inicial, data_final), step=timedelta(days=1))

# filtrar data
dados = dados.loc[intervalo_datas[0]:intervalo_datas[1]]
# filtrar ações
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes)==1:
        dados = dados.rename(columns={lista_acoes[0]: "Close"})
    

st.line_chart(dados)