# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 11

### Análise e Ciência de Dados via programação Python através de duas poderosas bibliotecas: Matplotlib e Seaborn ###

### MATPLOTLIB ###

# https://matplotlib.org/
# 
# Matplotlib é uma biblioteca de visualização de dados em Python amplamente utilizada para criar gráficos
# e visualizações de alta qualidade em diversas áreas, como ciência de dados, engenharia, finanças, estatística,
# entre outras. É uma biblioteca extremamente poderosa, flexível e personalizável, que permite a criação de
# gráficos em 2D e 3D, histogramas, diagramas de dispersão, gráficos de linhas, entre outros.
# 
# O Matplotlib oferece uma grande variedade de estilos de plotagem, tipos de gráficos e configurações de
# plotagem para personalização de gráficos. Ele é compatível com vários formatos de arquivos de imagem,
# como PNG, PDF, SVG, entre outros, permitindo a geração de imagens de alta qualidade para uso em publicações
# e apresentações.
# 
# Além disso, o Matplotlib é uma biblioteca de código aberto e gratuita, com uma comunidade ativa de
# desenvolvedores e usuários, o que significa que há uma grande quantidade de documentação, exemplos e suporte
# disponíveis online.

# O matplotlib.pyplot é uma coleção de funções e estilos do Matplotlib 
import matplotlib.pyplot as plt


# O método plot() define os eixos do gráfico
# figura 1
plt.plot([1, 3, 5], [2, 4, 7])
plt.show()


x = [2, 3, 5]
y = [3, 5, 7]

# figura 2
plt.plot(x, y)
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Teste Plot')
plt.show()


x2 = [1, 2, 3]
y2 = [11, 12, 15]

# figura 3
plt.plot(x2, y2, label = 'Gráfico com Matplotlib')
plt.legend()
plt.show()


### Gráfico de Barras ###

# Gráfico de barras é um tipo de plotagem usado para representar dados categóricos com barras
# retangulares. Cada barra representa uma categoria e a altura da barra representa a quantidade ou
# frequência da categoria.
# 
# O eixo horizontal do gráfico de barras mostra as categorias e o eixo vertical mostra a escala de
# medida dos dados. As barras podem ser vertical ou horizontal, dependendo da preferência do usuário.
# 
# Os gráficos de barras são comumente usados para comparar a quantidade ou frequência de diferentes
# categorias. Eles são úteis para mostrar diferenças entre grupos e ajudam a visualizar rapidamente
# quais categorias têm valores maiores ou menores.


x1 = [2,4,6,8,10]
y1 = [6,7,8,2,4]


# figura 4
plt.bar(x1, y1, label = 'Barras', color = 'green')
plt.legend()
plt.show()


x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

# figura 5
plt.bar(x1, y1, label = 'Listas1', color = 'blue')
plt.bar(x2, y2, label = 'Listas2', color = 'red')
plt.legend()
plt.show()








print("Os gráficos foram gerados")

print("-"*50)