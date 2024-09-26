# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 9

### Python para Análise de Dados, Ciência de Dados, Machine Learning e Inteligência Artificial == Pacote NumPy ###

# Importando o NumPy
import numpy as dsa
print(dsa.__version__)


### Manipulando Matrizes ###

# Criando uma matriz
arr9 = dsa.array( [ [1,2,3] , [4,5,6] ] )

print(type(arr9))

print(arr9)

print(arr9.shape)


# Criando uma matriz 2x3 apenas com números "1"
arr10 = dsa.ones((2,3))

print(arr10)


# Lista de listas
lista = [[13,81,22], [0, 34, 59], [21, 48, 94]]

# A função matrix cria uma matriz a partir de uma lista de listas
arr11 = dsa.matrix(lista)

print(type(arr11))

print(arr11)

# Formato da matriz
print(dsa.shape(arr11))

# Tamanho da matriz
print(arr11.size)

print(arr11.dtype)

print(arr11)

# Indexação da matriz
print(arr11[2,1])
print(arr11[0:2,2])
print(arr11[1,])

# Alterando um elemento da matriz
arr11[1,0] = 100
print(arr11)


x = dsa.array([1, 2])  # NumPy decide o tipo dos dado
y = dsa.array([1.0, 2.0])  # NumPy decide o tipo dos dado
z = dsa.array([1, 2], dtype = dsa.float64)  # Forçamos um tipo de dado em particular

print(x.dtype, y.dtype, z.dtype)
# resposta == int64 float64 float64


arr12 = dsa.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype = float)

print(arr12)

# O itemsize de um array numpy é um atributo que retorna o tamanho em bytes de cada elemento do array. Em
# outras palavras, o itemsize representa o número de bytes necessários para armazenar cada valor do array numpy.

print(arr12.itemsize)

print(arr12.nbytes)

print(arr12.ndim)


### Manipulando Objetos de 3 e 4 Dimensões com NumPy ###

# Cria um array numpy de 3 dimensões
arr_3d = dsa.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])

print(arr_3d)






print("-"*50)