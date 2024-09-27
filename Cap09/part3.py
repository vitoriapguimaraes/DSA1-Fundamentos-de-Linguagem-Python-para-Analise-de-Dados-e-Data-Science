# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 9

### Python para Análise de Dados, Ciência de Dados, Machine Learning e Inteligência Artificial == Pacote NumPy ###

# Importando o NumPy
import numpy as dsa


### Manipulando Arquivos com NumPy ###

import os
filename = os.path.join('Cap09/arquivos/dataset.csv')

# ver cabeçalho da tabela
import pandas as pd
df = pd.read_csv('Cap09/arquivos/dataset.csv')
print(df.head())


# Carregando um dataset para dentro de um array
arr13 = dsa.loadtxt(filename, delimiter = ',', usecols = (0,1,2,3), skiprows = 1)
    # usecols 0, 1, 2, 3 == ultima coluna é str
    # skiprows = 1 == para tirar o cabeçalho

print(arr13)

print(type(arr13))


# Carregando apenas duas variáveis (colunas) do arquivo
var1, var2 = dsa.loadtxt(filename, delimiter = ',', usecols = (0,1), skiprows = 1, unpack = True)

# Gerando um plot a partir de um arquivo usando o NumPy
import matplotlib.pyplot as plt

plt.plot(var1, var2, 'o', markersize = 6, color = 'red')
plt.show()