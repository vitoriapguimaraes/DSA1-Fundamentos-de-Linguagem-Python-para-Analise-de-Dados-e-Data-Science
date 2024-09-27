# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 10

### PANDAS ###
import pandas as pd
print(pd.__version__)
dsa_df = pd.read_csv("Cap10/arquivos/dataset.csv")

### Operadores Lógicos Para Manipulação de Dados com Pandas ###

# Os operadores lógicos são excelentes para filtrar dataframes e retornar exatamente os
# dados que precisamos para nosso trabalho. Para conhecer mais sobre as regras dos operadores lógicos,
# acesse aqui: https://pt.wikipedia.org/wiki/Operador_l%C3%B3gico
# 
# Primeiro usaremos o operador lógico AND para checar duas condições. Serão retornados os registros
# quando as duas condições forem verdadeiras.


# Filtrando as vendas que ocorreram para o segmento de Home Office e na região South
filtro_and = dsa_df[ (dsa_df.Segmento == 'Home Office') & (dsa_df.Regiao == 'South') ].head()
print(filtro_and)


# Mas pode ser necessário checar duas condições e retornar os registros se pelo menos uma for
# verdadeira. Nesse caso usamos o operador OR, conforme abaixo.

# Filtrando as vendas que ocorreram para o segmento de Home Office ou região South
filtro_or = dsa_df[(dsa_df.Segmento == 'Home Office') | (dsa_df.Regiao == 'South')].tail()
print(filtro_or)


# O operador de negação é o contrário do primeiro exemplo.

# Filtrando as vendas que não ocorreram para o segmento de Home Office e nem na região South
filtro_neg = dsa_df[(dsa_df.Segmento != 'Home Office') & (dsa_df.Regiao != 'South')].sample(5)
print(filtro_neg)


# head = primeiros | tail = finais | sample = aleatórios


### Agrupamento de Dados em DataFrames com Group By ###

# A função Pandas Groupby é uma função versátil e fácil de usar que ajuda a obter uma visão geral dos
# dados. Isso torna mais fácil explorar o conjunto de dados e revelar os relacionamentos entre as
# variáveis.
# 
# O código a seguir agrupará as linhas com base nas combinações Segmento/Regiao/Valor_Venda e nos dará
# a taxa média de vendas de cada grupo.

# Aplicamos o group by
df1 = dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean()
print(df1)

# Na instrução acima, primeiro filtramos os dados extraindo
# 3 colunas: ['Segmento','Regiao','Valor_Venda']. Na sequência, agrupamos por
# duas colunas: ['Segmento','Regiao'].
# E então calculamos a média para a coluna que ficou foram do group by, nesse caso a coluna Sales.
# 
# O comportamento do group by com Pandas é o mesmo observado na Linguagem SQL.


### Agregação Múltipla com Group By ###

# Vamos explorar mais a função groupby() pois temos diversas opções de sumarização dos dados de
# forma simples. No exemplo abaixo uniremos a função groupby() com a função agg() para realiza
# agregação múltipla.

# Aplicamos o group by
df2 = dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count'])
print(df2)

# Na instrução acima, primeiro filtramos os dados extraindo 
# colunas: ['Segmento','Regiao','Valor_Venda']. Na sequência, agrupamos por
# duas colunas: ['Segmento','Regiao'].
# E então agregamos os dados calculando a média, desvio padrão e contagem de elementos para a
# coluna que ficou fora do group by, nesse caso a coluna Valor_Venda.
# 
# A função agg() recebe como argumento uma lista de funções para agregação.