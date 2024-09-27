# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 10

### PANDAS ###
import pandas as pd
print(pd.__version__)

### Preenchendo Valores Ausentes em DataFrames do Pandas ###

# A função fillna() é usada para preencher os valores ausentes. A função oferece muitas opções. Podemos
# usar um valor específico, uma função agregada (por exemplo, média) ou o valor anterior ou seguinte.
# 
# Para esse exemplo usaremos a moda, a estatística que representa o valor que aparece mais vezes em uma
# variável.

# Primeiro importamos um dataset
dsa_df = pd.read_csv("Cap10/arquivos/dataset.csv")

print(dsa_df.head(5))

ausente = dsa_df.isna().sum()
print(ausente)

# Extraímos a moda da coluna Quantity
moda = dsa_df['Quantidade'].value_counts().index[0]


# A moda em Estatística é uma medida de tendência central que representa o valor mais frequente em um
# conjunto de dados.
# 
# A moda é especialmente útil quando queremos saber qual é o valor mais comum ou popular em um conjunto
# de dados, seja em uma distribuição unimodal (com apenas uma moda) ou em uma distribuição bimodal (com
# duas modas).
# 
# No entanto, a moda pode não ser tão representativa quanto outras medidas de tendência central, como a
# média e a mediana, especialmente em distribuições assimétricas ou quando há valores extremos. Por essa 
# razão, é importante analisar diferentes medidas de tendência central e usar a que melhor se adequa aos
# objetivos da análise estatística.

print(moda)

# E por fim preenchemos os valores NA com a moda
dsa_df['Quantidade'].fillna(value = moda, inplace = True)
    # inplace = True == para salvar no dataframe

ausente2 = dsa_df.isna().sum()
print(ausente2)


### Query (Consulta) de Dados no DataFrame do Pandas ###

# Com o Pandas criamos dataframes, que são essencialmente tabelas. Como tal, podemos fazer consultas,
# ou simplesmente queries. E para isso usamos o método query(). Veja o exemplo abaixo:

print(dsa_df.head())
# Checamos os valores mínimo e máximo da coluna Valor_Venda
print(dsa_df.Valor_Venda.describe())


# O intervalo de vendas (Valor_Venda) é de 0.44 a 22638. Vamos fazer uma consulta e retornar todas as
# vendas dentro de um range de valores. Fazemos isso com a instrução abaixo:

# Geramos um novo dataframe apenas com o intervalo de vendas entre 229 e 10000
df2 = dsa_df.query('229 < Valor_Venda < 10000')

# Então confirmamos os valores mínimo e máximo
print(df2.Valor_Venda.describe())


# Geramos um novo dataframe apenas com os valores de venda acima da média
df3 = df2.query('Valor_Venda > 766')

print(df3.head())

# Consulta executada com sucesso!


### Verificando a Ocorrência de Diversos Valores em Uma Coluna ###

# Em nosso conjunto de dados de exemplo temos a coluna Quantidade que representa a quantidade de itens
# vendidos em cada uma das vendas. Imagine que precisamos saber em quais vendas foram vendidos 5, 7, 9
# ou 11 itens.
# 
# Como aplicaríamos esse tipo de filtro ao nosso dataframe?
# 
# Fácil. O Pandas oferece o método isin() para checar diversos valores em uma coluna. Quem conhece
# Linguagem SQL já deve ter percebido que o método é o mesmo que a cláusula IN em SQL. Vamos ao exemplo.

print(dsa_df.shape)

# Então aplicamos o filtro
filtro = dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])]
print(filtro)


# Na instrução acima estamos filtrando o dataframe chamado df, retornando todas as linhas onde a coluna
# Quantidade for igual aos valores 5, 7, 9 ou 11. Passamos uma lista de valores como argumento para o
# método isin().
# 
# Vamos deixar um pouquinho mais divertido. Se você executou a instrução acima, percebeu que foram
# retornadas 2.128 linhas. E se quisermos retornar somente 10 linhas? É só fatiar o resultado assim:

# unindo os dois comandos anteriores:
filtro_shape = dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])].shape
print(filtro_shape)

# comando de cima, mostrando apenas as 10 primeiras linhas
filtro_shape_ = dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])][:10].shape
print(filtro_shape_)