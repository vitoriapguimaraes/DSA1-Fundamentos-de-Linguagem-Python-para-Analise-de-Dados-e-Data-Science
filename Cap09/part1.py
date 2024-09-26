# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 9

### Python para Análise de Dados, Ciência de Dados, Machine Learning e Inteligência Artificial == Pacote NumPy ###

# Importando o NumPy
import numpy as dsa
print(dsa.__version__)


### Criando Arrays NumPy ###

# Array criado a partir de uma lista Python
arr1 = dsa.array([10, 21, 32, 43, 48, 15, 76, 57, 89])

print(arr1)

# Um objeto do tipo ndarray é um recipiente multidimensional de itens do mesmo tipo e tamanho
print(type(arr1))

print(arr1.shape)


# Um array NumPy é uma estrutura de dados multidimensional usada em computação científica e análise de dados.
# O NumPy fornece um objeto de matriz N-dimensional (ou ndarray), que é uma grade homogênea de elementos,
# geralmente números, que podem ser indexados por um conjunto de inteiros.
# 
# Os arrays NumPy são mais eficientes do que as listas Python para armazenar e manipular grandes quantidades
# de dados, pois são implementados em Linguagem C e fornecem várias otimizações de desempenho. Além disso, o
# NumPy permite a fácil leitura e escrita de arquivos de dados, integração com outras bibliotecas Python e
# suporte a operações em paralelo usando várias CPUs ou GPUs.


### Indexação em Arrays NumPy ###

print(arr1)

# Imprimindo um elemento específico no array
print(arr1[4] )

# Indexação
print(arr1[1:4])

# Indexação
print(arr1[1:4+1])

# Cria uma lista de índices
indices = [1, 2, 5, 6]

# Imprimindo os elementos dos índices
arr1[indices] 

# Cria uma máscara booleana para os elementos pares
mask = (arr1 % 2 == 0)
print(arr1)
print(mask)

print(arr1[mask])


# Alterando um elemento do array
arr1[0] = 100

print(arr1)

# Não é possível incluir elemento de outro tipo
try:
    arr1[0] = 'Novo elemento'
except:
    print("Operação não permitida!")


### Funções NumPy ###

# A função array() cria um array NumPy
arr2 = dsa.array([1, 2, 3, 4, 5])

print(arr2)

# Verificando o tipo do objeto
print(type(arr2))


# Digite . e pressione a tecla Tab no seu teclado para visualizar os métodos disponíveis em objetos NumPy
arr2

# Usando métodos do array NumPy
print(arr2.cumsum())

print(arr2.cumprod())


# Digite . e pressione a tecla Tab no seu teclado para visualizar as funções para manipular objetos NumPy
dsa

# A função arange cria um array NumPy contendo uma progressão aritmética a partir de um intervalo -
# start, stop, step
arr3 = dsa.arange(0, 50, 5)

print(arr3)

# Verificando o tipo do objeto
print(type(arr3))

# Formato do array
print(dsa.shape(arr3))

print(arr3.dtype)


# Cria um array preenchido com zeros
arr4 = dsa.zeros(10)

print(arr4)


# Retorna 1 nas posições em diagonal e 0 no restante
arr5 = dsa.eye(3)

print(arr5)


# Os valores passados como parâmetro, formam uma diagonal
arr6 = dsa.diag(dsa.array([1, 2, 3, 4]))

print(arr6)


# Array de valores booleanos
arr7 = dsa.array([True, False, False, True])

print(arr7)


# Array de strings
arr8 = dsa.array(['Linguagem Python', 'Linguagem R', 'Linguagem Julia'])

print(arr8)


# A função linspace() do NumPy é usada para criar uma sequência de números igualmente espaçados dentro de um
# intervalo especificado. Essa função é amplamente utilizada em programação científica e matemática para gerar
# arrays de números para diversos fins, como gráficos, cálculos e simulações.
# 
# O método linspace (linearly spaced vector) retorna um número de valores igualmente distribuídos no intervalo
# especificado. 

print(dsa.linspace(0, 10))

print(dsa.linspace(0, 10, 15))


# A função logspace() do NumPy é usada para criar uma sequência de números igualmente espaçados em escala
# logarítmica dentro de um intervalo especificado. Essa função é amplamente utilizada em programação científica
# e matemática para gerar arrays de números para diversos fins, como gráficos, cálculos e simulações.

print(dsa.logspace(0, 5, 10))

print("-"*50)