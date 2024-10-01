# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 12

### Python e Linguagem SQL ###

# Para este capítulo usaremos o SQLite: https://sqlite.org/index.html
import sqlite3
import pandas as pd

print(sqlite3.sqlite_version)
print(pd.__version__)

### Aplicando Linguagem SQL na Sintaxe do Pandas com Linguagem Python ###

# Conecta no banco de dados
con = sqlite3.connect('Cap12/cap12_dsa.db')

# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

# > A query abaixo retorna todas as linhas e todas as colunas da tabela.
# Cria uma instrução SQL
query = 'SELECT * FROM tb_vendas_dsa'

# Executa a query no banco de dados
print(cursor.execute(query))

# Retorna os dados da execução da query
dados = cursor.fetchall()

# Visualiza os dados
print(dados)

print(type(dados))

print("-"*50)