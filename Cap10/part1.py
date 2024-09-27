# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 10

### PANDAS ###
import pandas as pd
print(pd.__version__)


### Manipulando Dados em DataFrames do Pandas ###

# Cria um dicionário
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'], 
         'Ano': [2004, 2005, 2006, 2007, 2008], 
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}

print(dados)

# Importa a função DataFrame do Pandas
from pandas import DataFrame

# Converte o dicionário em um dataframe
df1 = DataFrame(dados)

# Visualiza as 5 primeiras linhas
print(df1.head())

print(type(df1))


# Reorganizando as colunas
df1_1 = DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano'])

print(df1_1)


# Criando outro dataframe com os mesmo dados anteriores mas adicionando uma coluna
df2 = DataFrame(dados, 
                columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'], 
                index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])

print(df2)

print(df2.values)

print(df2.dtypes)

print(df2.columns)


# Imprimindo apenas uma coluna do Dataframe
print(df2['Estado'])

# Linguagem Python é case sensitive
# df2['estado']


# Imprimindo apenas duas colunas do Dataframe
print(df2[ ['Taxa Desemprego', 'Ano'] ])            # duas [[]]

print(df2.index)


# Filtrando pelo índice
df2_1 = df2.filter(items = ['estado3'], axis = 0)
print(df2_1)



print("-"*50)