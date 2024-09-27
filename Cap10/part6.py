# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 10

### PANDAS ###
import pandas as pd
print(pd.__version__)

import matplotlib.pyplot as plt


### Construção de Gráficos a Partir de DataFrames do Pandas ###

# Vimos até aqui diversas funcionalidades do Pandas que tornam o processo de manipulação de dados
# realmente simples. E para concluir este capítulo vamos estudar as opções que o Pandas oferece para
# criação de gráficos diretamente a partir de dataframes, sem a necessidade de usar qualquer outra
# biblioteca.
# 
# Acompanhe os exemplos.

import sklearn
print(sklearn.__version__)

# Vamos começar importando o dataset iris do Scikit-learn
from sklearn.datasets import load_iris
data = load_iris()

# E então carregamos o dataset iris como dataframe do Pandas
df = pd.DataFrame(data['data'], columns = data['feature_names'])
df['species'] = data['target']

print(df.head())

# Para criar um gráfico de linhas com todas as variáveis do dataframe, basta fazer isso:
# df.plot()
plt.show()


print("-"*50)