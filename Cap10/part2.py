# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 10

### PANDAS ###
import pandas as pd
print(pd.__version__)

from pandas import DataFrame

dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'], 
         'Ano': [2004, 2005, 2006, 2007, 2008], 
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}

df2 = DataFrame(dados, 
                columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'], 
                index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])


### Usando NumPy e Pandas para Manipulação de Dados ###

print(df2.head())
print(df2.dtypes)

# Resumo estatístico do Dataframe
print(df2.describe())


print(df2.isna())  # is na = tem valor ausente?

print(df2['Taxa Crescimento'].isna())

# Importando o NumPy
import numpy as np

# Usando o NumPy para alimentar uma das colunas do dataframe
df2['Taxa Crescimento'] = np.arange(5.)

print(df2)
print(df2.dtypes)

print(df2['Taxa Crescimento'].isna())

# Resumo estatístico do Dataframe
print(df2.describe())


### Slicing de DataFrames do Pandas ###

df2_1 = df2['estado2':'estado4']
print(df2_1)

df2_2 = df2[ df2['Taxa Desemprego'] < 2 ]
print(df2_2)

df2_3 = df2['Taxa Crescimento']
print(df2_3)

df2_4 = df2[['Estado', 'Taxa Crescimento']]
print(df2_4)

df2_5 = df2[['Estado', 'Taxa Crescimento', 'Ano']]
print(df2_5)