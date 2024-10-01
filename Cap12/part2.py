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


# Carrega os dados como dataframe do Pandas
df = pd.DataFrame(dados, columns = ['ID_Pedido', 
                                    'ID_Cliente', 
                                    'Nome_Produto',
                                    'Valor_Unitario',
                                    'Unidades_Vendidas',
                                    'Custo'])

print(df.head())


# Fecha o cursor e encerra a conexão
cursor.close()
con.close()


# > A query abaixo retorna a média de unidades vendidas.
# Calcula a média de unidades vendidas
media_unidades_vendidas = df['Unidades_Vendidas'].mean()

print(type(media_unidades_vendidas))
print(media_unidades_vendidas)


# > A query abaixo retorna a média de unidades vendidas por produto.
# Calcula a média de unidades vendidas por produto
media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()

# Visualiza os 10 primeiros resultados
print(media_unidades_vendidas_por_produto.head(10))


# > A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for
# maior do que 199.
# Retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199.
med199 = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print("med>199")
print(med199)

# > A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for
# maior do que 199 e somente se a média de unidades vendidas for maior do que 10.

# Alternativa A
altA = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10)
print("altA")
print(altA)

# Alternativa B
altB = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print("altB")
print(altB)



print("-"*50)