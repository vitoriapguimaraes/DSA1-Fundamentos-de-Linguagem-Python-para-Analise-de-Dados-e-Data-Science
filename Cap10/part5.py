# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 10

### PANDAS ###
import pandas as pd
print(pd.__version__)
dsa_df = pd.read_csv("Cap10/arquivos/dataset.csv")

### Filtrando DataFrame do Pandas com Base em Strings ###

# O Pandas oferece diversas funções para manipulação de strings. Começaremos com o
# filtros de strings com base nas letras iniciais e finais.

print(dsa_df.head())


# Filtramos o dataframe pela coluna Segmento com valores que iniciam com as letras 'Con'
filtro1 = dsa_df[dsa_df.Segmento.str.startswith('Con')].head()
print(filtro1)

# conferir se deu certo o comando anterior
print(dsa_df.Segmento.value_counts())


# Filtramos o dataframe pela coluna Segmento com valores que terminam com as letras 'mer'
filtro2 = dsa_df[dsa_df.Segmento.str.endswith('mer')].head()
print(filtro2)


# As funções startswith() e endswith() são muito úteis quando for necessário filtrar strings
# por caracteres que apareçam no começo e/ou final.


### Split de Strings em DataFrames do Pandas ###

# Com Pandas podemos realizar diversas tarefas de split de strings dividindo uma coluna ou
# extraindo elementos do nosso interesse. Vamos ao exemplo!

print(dsa_df.head())

filtro3 = dsa_df['ID_Pedido'].head()
print(filtro3)


# Este é o formato dos dados da coluna "ID_Pedido":
# - CA-2016-152156
# - US-2015-108966
# Temos o país, o ano e o id do pedido. Vamos dividir essa coluna e extrair o ano para gravar em
# uma nova coluna:

# Split da coluna pelo caracter '-'
spli1 = dsa_df['ID_Pedido'].str.split('-')
print(spli1)

# Observe que o resultado são as listas em Python. Para extrair o ano precisamos especificar o índice
# da posição que queremos extrair (em nosso caso a posição 2, logo, índice 1 em Python):

split2 = dsa_df['ID_Pedido'].str.split('-').str[1].head()
print(split2)


# Fazemos o split da coluna e extraímos o item na posição 2 (índice 1)
dsa_df['Ano'] = dsa_df['ID_Pedido'].str.split('-').str[1]

# Então conferimos a nova coluna criada
print(dsa_df.head())

# >>>>> Fizemos Engenharia de Atributos <<<<<<

### Strip de Strings em DataFrames do Pandas ###

# Cuidado para não confundir. Vimos o Split e agora veremos o Strip. São funções diferentes.
# O Split divide a string. O Strip remove caracteres da string. Veja os exemplos.

print(dsa_df.head(3))

print(dsa_df['Data_Pedido'].head(3))

# A coluna 'Data_Pedido' é a data de envio do produto no formato YYYY-MM-DD. Imagine que seja
# necessário deixar o ano apenas com 2 dígitos sem alterar o tipo da variável. Fazemos isso com a
# função lstrip(), ou seja, left strip.

# Vamos remover os dígitos 2 e 0 à esquerda do valor da variável 'Data_Pedido'
filtro4 = dsa_df['Data_Pedido'].str.lstrip('20')
print(filtro4)

# Como não usamos o inplace = True a mudança é somente na memória e não altera o dataframe. Podemos
# usar ainda as funções rstrip() e strip() com diferentes variações de strip de strings.

print(dsa_df['Data_Pedido'].head(3))


### Replace de Strings em DataFrames do Pandas ###

# Se for necessário substituir caracteres dentro de uma string o Pandas oferece uma função para isso
# também.
# 
# Por exemplo, vamos substituir 2 caracteres em uma das colunas.

print(dsa_df.head())

# Substituímos os caracteres CG por AX na coluna 'ID_Cliente'
dsa_df['ID_Cliente'] = dsa_df['ID_Cliente'].str.replace('CG', 'AX')

print(dsa_df.head())


### Combinação de Strings em DataFrames do Pandas ###

# A função cat() pode ser usada para concatenar strings em um dataframe do Pandas.
# 
# Vamos criar uma nova coluna concatenando as colunas “ID_Pedido” e “Segmento” com o separador “-”.

print(dsa_df.head())

# Concatenando strings
dsa_df['Pedido_Segmento'] = dsa_df['ID_Pedido'].str.cat(dsa_df['Segmento'], sep = '-')

print(dsa_df.head())