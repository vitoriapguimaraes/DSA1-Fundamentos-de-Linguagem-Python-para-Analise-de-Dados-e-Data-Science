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

# Query SQL para extrair os nomes das colunas no banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""

# Executa a query
print(cursor.execute(sql_query))

# Visualiza o resultado
print(cursor.fetchall())

# > A query abaixo retorna todas as linhas e todas as colunas da tabela.
# Cria uma instrução SQL
query1 = 'SELECT * FROM tb_vendas_dsa'

# Executa a query no banco de dados
print(cursor.execute(query1))

# List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]

# Visualiza o resultado
print(nomes_colunas)

# Retorna os dados da execução da query
dados = cursor.fetchall()

# Visualiza os dados
print(dados)


### Aplicando Linguagem SQL Direto no Banco de Dados com Linguagem Python ###


# > A query abaixo retorna a média de unidades vendidas.
# Cria uma instrução SQL para calcular a média de unidades vendidas
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'

# Executa a query no banco de dados
print(cursor.execute(query2))

# Visualiza o resultado
print(cursor.fetchall())


# > A query abaixo retorna a média de unidades vendidas por produto.
# Cria uma instrução SQL para calcular a média de unidades vendidas por produto
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'

# Executa a query no banco de dados
print(cursor.execute(query3))

# Visualiza o resultado
print(cursor.fetchall())


# > A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for
# maior do que 199.
# Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
# quando o valor unitário for maior que 199
query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto"""

# Executa a query no banco de dados
print(cursor.execute(query4))

# Visualiza o resultado
print(cursor.fetchall())


# > A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for
# maior do que 199 e somente se a média de unidades vendidas for maior do que 10.
# Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
# quando o valor unitário for maior que 199, mas somente se a média de unidades vendidas for maior que 10
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto 
            HAVING AVG(Unidades_Vendidas) > 10"""
            
# Executa a query no banco de dados
print(cursor.execute(query5))

# Visualiza o resultado
print(cursor.fetchall())


# Fecha o cursor e encerra a conexão
cursor.close()
con.close()

print("-"*50)