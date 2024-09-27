# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 9

### Python para Análise de Dados, Ciência de Dados, Machine Learning e Inteligência Artificial == Pacote NumPy ###

# Importando o NumPy
import numpy as dsa


### Slicing (fatiamento) de Arrays NumPy ###

# Cria um array
arr22 = dsa.diag(dsa.arange(3))
print(arr22)

print(arr22[1, 1])

print(arr22[1])

print(arr22[:,2])


arr23 = dsa.arange(10)
print(arr23)

# [start:end:step]
print(arr23[2:9:3])


# Cria 2 arrays
a = dsa.array([1, 2, 3, 4])
b = dsa.array([4, 2, 2, 4])


# Comparação item a item
print(a == b)

# Comparação global
print(dsa.array_equal(arr22, arr23))


print(arr23.min())

print(arr23.max())


# Somando um valor a cada elemento do array
arr_soma = dsa.array([1, 2, 3]) + 1.5
print(arr_soma)


# Cria um array
arr24 = dsa.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])
print(arr24)

# Usando o método around
arr25 = dsa.around(arr24)
print(arr25)


# Criando um array
arr26 = dsa.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr26)

# O método flatten() com NumPy é usado para criar uma cópia unidimensional (ou "achatada") de um array
# multidimensional. Isso significa que o método cria um novo array unidimensional, que contém todos os elementos
# do array multidimensional original, mas que está organizado em uma única linha. A ordem dos elementos no novo
# array unidimensional segue a ordem dos elementos no array multidimensional original.

# "Achatando" a matriz
arr27 = arr26.flatten()
print(arr27)


# Criando um array
arr28 = dsa.array([1, 2, 3])
print(arr28)

# Repetindo os elementos de um array
arr28_1 = dsa.repeat(arr28, 3)
print(arr28_1)

# Repetindo os elementos de um array
arr28_2 = dsa.tile(arr28, 3)
print(arr28_2)


# Criando um array
arr29 = dsa.array([5, 6])

# Criando cópia do array
arr30 = dsa.copy(arr29)
print(arr30)