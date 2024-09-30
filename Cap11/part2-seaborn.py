# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 11

### Análise e Ciência de Dados via programação Python através de duas poderosas bibliotecas: Matplotlib e Seaborn ###

### SEABORN ###

# Imports
import random
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

print(np.__version__)
print(pd.__version__)
print(mat.__version__)

import seaborn as sea
print(sea.__version__)


### Criando Gráficos com Seaborn ###

# Carregando um dos datasets que vem com o Seaborn
dados = sea.load_dataset("tips")
print(dados.head())

# O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
sea.jointplot(data = dados, x = "total_bill", y = "tip", kind = 'reg')
# figura 1
plt.show()

# O método lmplot() cria plot com dados e modelos de regressão
sea.lmplot(data = dados, x = "total_bill", y = "tip", col = "smoker")
# figura 2
plt.show()


# Construindo um dataframe com Pandas
df = pd.DataFrame()

# Alimentando o Dataframe com valores aleatórios
df['idade'] = random.sample(range(20, 100), 30)
df['peso'] = random.sample(range(55, 150), 30)

print(df.shape)
print(df.head())

# lmplot
sea.lmplot(data = df, x = "idade", y = "peso", fit_reg = True)
# figura 3
plt.show()

# kdeplot
sea.kdeplot(df.idade)
# figura 4
plt.show()

# distplot
sea.distplot(df.peso)
# figura 5
plt.show()

# Histograma
plt.hist(df.idade, alpha = .3)
sea.rugplot(df.idade)
# figura 6
plt.show()

# Box Plot
sea.boxplot(df.idade, color = 'm')
# figura 7
plt.show()

# Box Plot
sea.boxplot(df.peso, color = 'y')
# figura 8
plt.show()

# Violin Plot
sea.violinplot(df.idade, color = 'g')
# figura 9
plt.show()

# Violin Plot
sea.violinplot(df.peso, color = 'cyan')
# figura 10
plt.show()

# Clustermap
sea.clustermap(df)
# figura 11
plt.show()

print("Os gráficos foram gerados")

print("-"*50)