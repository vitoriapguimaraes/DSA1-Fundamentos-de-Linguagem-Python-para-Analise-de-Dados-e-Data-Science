### Análise de dados associados a perguntas de negócios ###
### Análise Exploratória de Dados em Linguagem Python Para a Área de Varejo ###

# Fonte: https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxls


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


### Carregando os dados com pandas em Linguagem Python ###

df = pd.read_csv("Cap13/dados/dataset.csv")

print(f"\nShape dos dados é {df.shape}")
print("\nPrimeiras linhas dos dados:")
print(df.head())
print("\nÚltimas linhas dos dados:")
print(df.tail())

caminho = (f'Cap13/graficos')

### Análise exploratória ###

# Colunas do conjunto de dados
print(f"\nAs colunas do conjunto de dados são {df.columns}")

# Verificando o tipo de dado de cada coluna
print("\nCujo tipo de dados são:")
print(df.dtypes)

# Resumo estatístico da coluna com o valor de venda
print("\nResumo estatístico da coluna com o valor de venda:")
print(df['Valor_Venda'].describe())

# Verificando se há registros duplicados
print(f"\nRegistros duplicados: {df[df.duplicated()]}")

# Verificando de há valores ausentes
print(f"\nValores ausentes: \n{df.isnull().sum()}")


### Perguntas de Negócio ###


print("\nPergunta de Negócio 1")
print("Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?")

df_p1 = df[df['Categoria'] == 'Office Supplies']

df_p1_total = df_p1.groupby("Cidade")["Valor_Venda"].sum()

cidade_maior_venda = df_p1_total.idxmax()

print(f"\n>>> A Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supllies' é {cidade_maior_venda} <<<")

print(f"\nPara conferir o resultado, segue a lista do maior para menor: \n{df_p1_total.sort_values(ascending = False)}")


print("\nPergunta de Negócio 2")
print("Qual o Total de Vendas Por Data do Pedido?")
print("Demonstre o resultado através de um gráfico de barras.")

df_p2 = df.groupby("Data_Pedido")["Valor_Venda"].sum()
print(f"\n>>> Total de Vendas por Data do Pedido (primeiras cinco linhas): <<<\n{df_p2.head()}")

plt.figure(figsize= (12,6))
df_p2.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'blue')
plt.title('Total de Vendas Por Data do Pedido')
plt.xlabel("Data do Pedido")
plt.ylabel("Total do Valor de Venda (R$)")
plt.savefig(f"{caminho}/Pergunta 2")
# plt.show()
print(f"\nGráfico da Pergunta 2 exportado para {caminho}")


print("\nPergunta de Negócio 3")
print("Qual o Total de Vendas por Estado?")
print("Demonstre o resultado através de um gráfico de barras.")

df_p3 = df.groupby("Estado")["Valor_Venda"].sum().reset_index()
print(f"\n>>> Total de Vendas por Estado (primeiras cinco linhas): <<<\n{df_p3.head()}")

plt.figure(figsize= (12,12))
sns.barplot(data=df_p3,
            x = 'Estado',
            y = 'Valor_Venda',
            hue= 'Estado',
            palette=sns.color_palette("husl", n_colors=49, as_cmap=False),
            dodge=False,
            legend=False).set(title = "Total de Vendas Por Estado")
plt.xlabel("Estado")
plt.ylabel("Total do Valor de Venda (R$)")
plt.xticks(rotation = 80)
plt.savefig(f"{caminho}/Pergunta 3")
# plt.show()
print(f"\nGráfico da Pergunta 3 exportado para {caminho}")


print("\nPergunta de Negócio 4")
print("Quais São as 10 Cidades com Maior Total de Vendas?")
print("Demonstre o resultado através de um gráfico de barras.")

df_p4 = df.groupby("Cidade")["Valor_Venda"].sum().reset_index().sort_values(by="Valor_Venda", ascending = False)[0:10]

print(f"\n>>> As 10 Cidades com Maior Total de Vendas: <<<\n{df_p4}")

plt.figure(figsize= (12,8))
sns.barplot(data=df_p4,
            x = 'Cidade',
            y = 'Valor_Venda',
            hue= 'Cidade',
            palette=sns.color_palette("Set1", n_colors=10, as_cmap=False),
            dodge=False,
            legend=False).set(title = "As 10 Cidades com Maior Total de Vendas")
plt.xlabel("Cidade")
plt.ylabel("Total do Valor de Venda (R$)")
plt.xticks(rotation = 45)
plt.savefig(f"{caminho}/Pergunta 4")
# plt.show()
print(f"\nGráfico da Pergunta 4 exportado para {caminho}")


print("\nPergunta de Negócio 5")
print("Qual Segmento Teve o Maior Total de Vendas?")
print("Demonstre o resultado através de um gráfico de pizza.")

df_p5 = df.groupby("Segmento")["Valor_Venda"].sum().reset_index().sort_values(by= 'Valor_Venda', ascending= False)
df_p5['Valor_Venda_Formatado'] = df_p5['Valor_Venda'].apply(lambda x: f'{x:,.2f}')
df_p5_lista = df_p5["Segmento"].to_list()

print(f"\n>>> O Segmento com Maior Total de Vendas foi {df_p5_lista[0]}")

print(f"\n>>> Segmentos com Maiores Vendas: <<<\n{df_p5[['Segmento', 'Valor_Venda_Formatado']]}")

def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return f'{pct:.1f}%\nR$ {val:,.0f}'
    return my_format

plt.figure(figsize= (12,6))
plt.pie(df_p5["Valor_Venda"],
        labels = df_p5['Segmento'],
        autopct=autopct_format(df_p5['Valor_Venda']),
        startangle = 90)
plt.title("Segmentos com Maiores Vendas")
plt.axis('equal')

centre_circle = plt.Circle((0, 0), 0.88, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.savefig(f"{caminho}/Pergunta 5")
# plt.show()
print(f"\nGráfico da Pergunta 5 exportado para {caminho}")


print("\nPergunta de Negócio 6")
print("Qual o Total de Vendas Por Segmento e Por Ano")

df['Ano'] = df['ID_Pedido'].str.split('-').str[1].astype(int)
# Conferindo a nova coluna criada
# print(df.head())
# print(df.dtypes)

df_p6 = df.groupby(["Ano", "Segmento"])["Valor_Venda"].sum().reset_index()
print(f"\n>>> Total de Vendas Por Segmento e Por Ano: <<<\n{df_p6}")


print("\nPergunta de Negócio 7")
print("""Os gestores da empresa estão considerando conceder diferentes faixas de descontos e
gostariam de fazer uma simulação com base na regra abaixo:
    Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
    Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
Quantas Vendas Receberiam 15% de Desconto?""")

df['Desconto'] = np.where(df['Valor_Venda'] > 1000, 0.15, 0.10)
df_p7 = df['Desconto'].value_counts().tolist()
print(f"\n>>> No Total {df_p7[1]} Vendas Receberiam Desconto de 15%. <<<")


print("\nPergunta de Negócio 7")
print("""Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior.
Qual seria a Média do Valor de Venda Antes e Depois do Desconto?""")

print(df.head())

df['Valor_Venda_Desconto'] = df['Valor_Venda']*(1-df['Desconto'])

print(df.head())

# pegar média da coluna valor_venda e média valor_venda_desconto

print(f"\nO ")
print(df['Valor_Venda'].mean())
print(df['Valor_Venda_Desconto'].mean()) ### erro: empresa concedeu só o de 15%
# arrumar amanhã










# Pergunta de Negócio 9 (Desafio Nível Master Ninja):

#    Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?
#    Demonstre o resultado através de gráfico de linha.

# Pergunta de Negócio 10 (Desafio Nível Master Ninja das Galáxias):

#    Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias?
#    Demonstre tudo através de um único gráfico.