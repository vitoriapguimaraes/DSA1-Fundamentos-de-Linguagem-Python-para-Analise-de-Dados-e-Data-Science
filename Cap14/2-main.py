# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 14

### Análise estatística com o pacote Statsmodels em Linguagem Python ###

### Análise Estatística com Statsmodels ###

print("\n>>> Problema de Negócio: <<<")
print("""Existe alguma relação entre a área de imóveis (em metros quadrados) e o valor do aluguel em uma determinada cidade?
Caso exista relação, como podemos mensurá-la?""")
print("\n")

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


# Carrega o dataset
df_dsa = pd.read_csv('Cap14/dataset.csv')

print(df_dsa.shape)

print(df_dsa.columns)

print(df_dsa.head())