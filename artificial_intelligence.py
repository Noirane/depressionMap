import joblib
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.ticker import PercentFormatter
import json
import zipfile
import os

def graph_models():
    # Carregar as métricas dos modelos a partir do arquivo JSON
    with open('metricas_modelos.json', 'r') as f:
        resultados = json.load(f)

    # Plotar o gráfico de barras
    fig, ax = plt.subplots()
    modelos = list(resultados.keys())
    acuracias = list(resultados.values())
    
    barras = ax.bar(modelos, acuracias, color='orange')
    ax.set_xlabel('Models')
    ax.set_ylabel('Accuracy (%)')  # Indica que os valores estão em porcentagem
    ax.set_title('Accuracy in Predicting Depression Level')

    # Ajustar a rotação dos rótulos do eixo x
    plt.xticks(rotation=45, ha='right')

    # Adicionar o valor da acurácia em cima de cada barra com fonte menor
    for barra in barras:
        altura = barra.get_height()
        ax.text(barra.get_x() + barra.get_width() / 2.0, altura, f'{altura * 100:.2f}%', 
                ha='center', va='bottom', fontsize=8)  # Ajuste o tamanho da fonte aqui

    # Configurar o eixo y para exibir como porcentagem com duas casas decimais
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=2))

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)

def plot_shap_summary():
    # Carregar as informações do gráfico a partir do arquivo JSON
    with open('grafico_info.json', 'r') as f:
        grafico_info = json.load(f)

    # Criar o gráfico de barras com os dados carregados do JSON
    fig, ax = plt.subplots(figsize=grafico_info['figsize'])
    
    # Criar o gráfico de barras horizontais
    ax.barh(grafico_info['features'], grafico_info['mean_abs_shap_values'], color=grafico_info['color'])
    
    # Aumentando o tamanho da fonte dos rótulos e título
    ax.set_xlabel(grafico_info['xlabel'], fontsize=16)
    ax.set_ylabel(grafico_info['ylabel'], fontsize=16)
    ax.set_title(grafico_info['title'], fontsize=16)
    plt.gca().invert_yaxis()  # Inverter o eixo y para mostrar as variáveis mais importantes no topo
    plt.tight_layout()

    # Aumentar o tamanho da fonte dos rótulos das features no eixo y
    ax.set_yticklabels(grafico_info['features'], fontsize=16)  # Defina o tamanho desejado da fonte aqui

    # Adicionar rótulos nos valores para cada barra com 4 casas decimais e aumentar a fonte
    for index, value in enumerate(grafico_info['mean_abs_shap_values']):
        ax.text(value, index, f'{value:.4f}', va='center', fontsize=10)  # Aumentando o tamanho da fonte dos rótulos

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)

