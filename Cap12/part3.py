# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 12

### Python e Linguagem SQL ###

# Para este capítulo usaremos o SQLite: https://sqlite.org/index.html
import sqlite3
import pandas as pd

print(sqlite3.sqlite_version)
print(pd.__version__)

### Sintaxe SQL x Sintaxe Pandas ###

# Conecta no banco de dados
con = sqlite3.connect('Cap12/cap12_dsa.db')

# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

### As duas instruções abaixo retornam o mesmo resultado! ###

print("Sintaxe SQL")
                         
# Sintaxe SQL
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto 
            HAVING AVG(Unidades_Vendidas) > 10"""
# Executa a query no banco de dados
cursor.execute(query5)
# Visualiza o resultado
print(cursor.fetchall())


print("Sintaxe Pandas")                         

query = 'SELECT * FROM tb_vendas_dsa'
cursor.execute(query)
dados = cursor.fetchall()

# Carrega os dados como dataframe do Pandas
df = pd.DataFrame(dados, columns = ['ID_Pedido', 
                                    'ID_Cliente', 
                                    'Nome_Produto',
                                    'Valor_Unitario',
                                    'Unidades_Vendidas',
                                    'Custo'])

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()

# Sintaxe Pandas
pandas1 = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean()

print(pandas1)

print("-"*50)