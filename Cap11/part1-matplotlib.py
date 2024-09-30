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


idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]

ids = [x for x in range(len(idades))]
print(ids)

# figura 6
plt.bar(ids, idades)
plt.show()


bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

# figura 7
plt.hist(idades, bins, histtype = 'bar', rwidth = 0.8)
plt.show()

# figura 8
plt.hist(idades, bins, histtype = 'stepfilled', rwidth = 0.8)
plt.show()


### Gráfico de Dispersão ###

# Gráfico de dispersão, também conhecido como gráfico de pontos, é um tipo de plotagem utilizado
# para representar a relação entre duas variáveis contínuas. Cada ponto no gráfico de dispersão
# representa um par de valores das duas variáveis, onde uma variável é plotada no eixo horizontal
# e outra no eixo vertical.


x = [1,2,3,4,5,6,7,8]
y = [5,2,4,5,6,8,4,8]

# figura 9
plt.scatter(x, y, label = 'Pontos', color = 'r', marker = 'o')
plt.legend()
plt.show()


### Gráfico de Área Empilhada ###

# Stack plots, também conhecidos como gráficos de área empilhada, são um tipo de plotagem usados
# para visualizar a mudança relativa de diversas variáveis ao longo do tempo. Eles consistem em
# várias áreas coloridas empilhadas umas sobre as outras, onde a altura de cada área representa
# a magnitude da variável correspondente e a largura representa a escala de tempo.
# 
# Os stack plots são úteis para mostrar como as partes contribuem para o todo ao longo do tempo.
# Por exemplo, eles podem ser usados para visualizar a mudança relativa de diferentes setores de
# uma indústria ao longo do tempo, ou a distribuição relativa de receitas e despesas de uma empresa
# em um determinado período.


dias = [1,2,3,4,5]
dormir = [7,8,6,77,7]
comer = [2,3,4,5,3]
trabalhar = [7,8,7,2,2]
passear = [8,5,7,8,13]

# figura 10
plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m','c','r','k','b'])
plt.show()


### Gráfico de Pizza ###

# Gráfico de Pizza (Pie Plot), também conhecido como gráfico de setores, é um tipo de plotagem que
# representa a composição de uma variável categórica em relação ao todo. Ele é representado por um
# círculo dividido em fatias que representam as proporções relativas das categorias.
# 
# Cada fatia do gráfico de pizza corresponde a uma categoria e sua área é proporcional à porcentagem
# que a categoria representa do todo. A categoria mais representativa é geralmente posicionada na
# parte superior do círculo, enquanto as outras fatias são posicionadas em sentido horário.
# 
# Os gráficos de pizza são comumente usados para mostrar a distribuição de dados em relação ao todo
# e para destacar as proporções relativas de diferentes categorias. Por exemplo, um gráfico de pizza
# pode ser usado para mostrar a distribuição de vendas por produto em uma empresa ou a distribuição
# de votos por partido em uma eleição.


fatias = [7, 2, 2, 13]
atividades = ['dormir', 'comer', 'passear', 'trabalhar']
cores = ['olive', 'lime', 'violet', 'royalblue']

# figura 11
plt.pie(fatias,
        labels = atividades, colors = cores,
        startangle = 90, shadow = True, explode = (0,0.2,0,0))
plt.show()


### Criando Gráficos Customizados com Pylab ###

# Pylab é um módulo fornecido pela biblioteca Matplotlib que combina a funcionalidade do pacote
# NumPy com a funcionalidade do pacote pyplot. Ele fornece um ambiente de plotagem interativo,
# permitindo que os usuários criem rapidamente gráficos e visualizações de dados.
# 
# O módulo Pylab inclui muitas funções úteis para plotagem de gráficos, como funções para criar
# gráficos de linha, gráficos de dispersão, gráficos de barras, gráficos de pizza, histogramas e
# muito mais. Ele também fornece funções para personalizar as configurações de plotagem, como
# títulos de eixo, rótulos de eixo, títulos de gráfico e cores.

# O Pylab combina funcionalidades do pyplot com funcionalidades do Numpy
from pylab import *


### Gráfico de Linha ###

# Gráfico de linha é um tipo de plotagem usado para representar a evolução do comportamento
# de uma variável com diferentes pontos de dados. O gráfico normalmente é usado com variáveis
# contínuas.
# 
# No gráfico de linha, cada ponto de dados é representado por um ponto na linha. A linha
# conecta os pontos de dados.
# 
# Os gráficos de linha são úteis para visualizar tendências e padrões em dados contínuos ao
# longo do tempo. Por exemplo, eles podem ser usados para mostrar a variação da temperatura
# ao longo de um período de tempo, a evolução da população em uma região ou a flutuação do
# valor de uma ação na bolsa de valores.


# Gráfico de linha

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria a figura
fig = plt.figure()

# Define a escala dos eixos
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Cria o plot
axes.plot(x, y, 'r')

# Labels e título
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha');

# figura 12
plt.show()


# Gráficos de linha com 2 figuras

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria a figura
fig = plt.figure()

# Cria os eixos
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # eixos da figura principal
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # eixos da figura secundária

# Figura principal
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Figura Principal')

# Figura secundária
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('Figura Secundária');

# figura 13
plt.show()


# Gráficos de linha em Paralelo

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Divide a área de plotagem em dois subplots
fig, axes = plt.subplots(nrows = 1, ncols = 2)

# Loop pelos eixos para criar cada plot
for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Título')
    
# Ajusta o layout
fig.tight_layout()

# figura 14
plt.show()


# Gráficos de linha com diferentes escalas

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria os subplots
fig, axes = plt.subplots(1, 2, figsize = (10,4))
      
# Cria o plot1
axes[0].plot(x, x**2, x, exp(x))
axes[0].set_title("Escala Padrão")

# Cria o plot2
axes[1].plot(x, x**2, x, exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Escala Logaritmica (y)");

# figura 15
plt.show()


# Grid

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria os subplots
fig, axes = plt.subplots(1, 2, figsize = (10,3))

# Grid padrão
axes[0].plot(x, x**2, x, x**3, lw = 2)
axes[0].grid(True)

# Grid customizado
axes[1].plot(x, x**2, x, x**3, lw = 2)
axes[1].grid(color = 'b', alpha = 0.7, linestyle = 'dashed', linewidth = 0.8)

# figura 16
plt.show()


# Diferentes estilos de Plots

# Dados
xx = np.linspace(-0.75, 1., 100)
n = np.array([0,1,2,3,4,5])

# Subplots
fig, axes = plt.subplots(1, 4, figsize = (12,3))

# Plot 1
axes[0].scatter(xx, xx + 0.25 * randn(len(xx)), color = "black")
axes[0].set_title("scatter")

# Plot 2
axes[1].step(n, n ** 2, lw = 2, color = "blue")
axes[1].set_title("step")

# Plot 3
axes[2].bar(n, n ** 2, align = "center", width = 0.5, alpha = 0.5, color = "magenta")
axes[2].set_title("bar")

# Plot 4
axes[3].fill_between(x, x ** 2, x ** 3, alpha = 0.5, color = "green");
axes[3].set_title("fill_between");

# figura 17
plt.show()


### Histogramas ###

# Histogramas são um tipo de plotagem utilizado para visualizar a distribuição de uma
# variável contínua. Eles são compostos por barras retangulares adjacentes, onde a área de
# cada barra é proporcional à frequência de observações de dados que caem em uma faixa
# específica de valores.
# 
# No histograma, a variável contínua é dividida em faixas de valores, conhecidas como
# intervalos de classe. O eixo horizontal representa os intervalos de classe, enquanto o
# eixo vertical representa a frequência de observações de dados que caem em cada intervalo
# de classe. Os intervalos de classe devem ser escolhidos de forma apropriada para a
# distribuição dos dados e a escala dos eixos deve ser definida adequadamente.
# 
# Os histogramas são úteis para visualizar a forma e a dispersão de uma distribuição de
# dados contínuos, como a altura de uma população ou as pontuações de um teste. Eles podem
# ajudar a identificar a presença de valores atípicos ou outliers nos dados e fornecer
# insights importantes sobre a distribuição dos dados.

# Histogramas

# Dados
n = np.random.randn(100000)

# Cria os subplots
fig, axes = plt.subplots(1, 2, figsize = (12,4))

# Plot 1
axes[0].hist(n)
axes[0].set_title("Histograma Padrão")
axes[0].set_xlim((min(n), max(n)))

# Plot 2
axes[1].hist(n, cumulative = True, bins = 50)
axes[1].set_title("Histograma Cumulativo")
axes[1].set_xlim((min(n), max(n)));

# figura 18
plt.show()


### Gráficos 3D ###

from mpl_toolkits.mplot3d.axes3d import Axes3D

# Dados
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

# Função para um mapa de cores
def ColorMap(phi_m, phi_p):
    return ( + alpha - 2 * np.cos(phi_p)*cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p))

# Mais dados
phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = ColorMap(X, Y).T

# Cria a figura
fig = plt.figure(figsize = (14,6))

# Adiciona o subplot 1 com projeção 3d
ax = fig.add_subplot(1, 2, 1, projection = '3d')
p = ax.plot_surface(X, Y, Z,
                    rstride=4,
                    cstride=4,
                    linewidth=0)

# Adiciona o subplot 2 com projeção 3d
ax = fig.add_subplot(1, 2, 2, projection = '3d')
p = ax.plot_surface(X, Y, Z,
                    rstride=1,
                    cstride=1,
                    cmap=cm.coolwarm,
                    linewidth=0,
                    antialiased=False)

# Cria a barra de cores como legenda
cb = fig.colorbar(p, shrink=0.5)

# figura 19
plt.show()


# Wire frame

# Cria a figura
fig = plt.figure(figsize=(8,6))

# Subplot
ax = fig.add_subplot(1, 1, 1, projection = '3d')

# Wire frame
p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)

# figura 20
plt.show()

print("Os gráficos foram gerados")

print("-"*50)