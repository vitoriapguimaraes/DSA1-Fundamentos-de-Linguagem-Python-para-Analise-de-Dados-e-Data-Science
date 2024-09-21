# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 6

### PARTE 1 == MANIPULAÇÃO DE ARQUIVOS, parte 1 ###

### Lendo Arquivos ###

# Abrindo o arquivo para leitura

arq1 = open("Cap06/arquivos/arquivo1.txt", "r")

print(type(arq1))

# Lendo o arquivo
print(arq1.read())

# Contar o número de caracteres
print(arq1.tell())

# Lendo o arquivo
print(arq1.read()) # não tem nada porque o cursor está no final do arquivo

# Retornar para o iníco do arquivo
print(arq1.seek(0,0))

# Lendo o arquivo
print(arq1.read(23))

# Lendo o arquivo
print(arq1.read())


### Gravando Arquivos ###
# r = read
# w = write e sobrescreve
# a = append

# Abrindo arquivo para gravação
arq2 = open("Cap06/arquivos/arquivo2.txt", "w") # w = write

# Como abrimos o arquivo apenas para gravação, não podemos usar comandos de leitura.
# print(arq2.read()) #io.UnsupportedOperation: not readable

# Gravando arquivo
arq2.write("Aprendendo a programar em Python.")
arq2.close()

# Lendo arquivo gravado
arq2 = open("Cap06/arquivos/arquivo2.txt", "r")
print(arq2.read())

# Acrescentando conteúdo
arq2 = open("Cap06/arquivos/arquivo2.txt", "a") # a = append
arq2.write(" E a metodologia de ensino da Data Science Academy facilita o aprendizado.")
arq2.close()

arq2 = open("Cap06/arquivos/arquivo2.txt", "r")
print(arq2.read())

# Retornando ao início do arquivo para leitura
arq2.seek(0,0)
print(arq2.read())


print("-"*50)


### Abrindo Dataset em Linha Única ###

# Este arquivo abaixo foi obtido no site de dados abertos do governo da cidade de Chicago, nos EUA: 
# https://data.cityofchicago.org/

f = open("Cap06/arquivos/salarios.csv", "r")

data = f.read()

rows = data.split("\n")

# print(rows)

### Dividindo um Arquivo em Colunas ###

f = open("Cap06/arquivos/salarios.csv", "r")

data = f.read()

rows = data.split("\n")

full_data = []

print(type(rows))

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

print(full_data)


### Contando as Linhas de Um Arquivo ###

f = open("Cap06/arquivos/salarios.csv", "r")
data = f.read()
rows = data.split("\n")
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

count = 0
for row in full_data:
    count += 1 # equivalente a: count = count + 1

print(count)

### Contando as Colunas de Um Arquivo ###

f = open("Cap06/arquivos/salarios.csv", "r")
data = f.read()
rows = data.split("\n")
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data [0]
count = 0

for column in first_row:
    count += 1

print(count)


### Importando um Dataset com Pandas ###

import pandas as pd

arquivo = "Cap06/arquivos/salarios.csv"

df = pd.read_csv(arquivo) #df = dataframe

print(df)

df.head()

print(df['Position Title'].value_counts())