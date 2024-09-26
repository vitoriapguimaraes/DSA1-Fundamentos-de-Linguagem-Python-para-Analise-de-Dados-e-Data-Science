# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 9

### Python para Análise de Dados, Ciência de Dados, Machine Learning e Inteligência Artificial == Pacote NumPy ###

# Importando o NumPy
import numpy as dsa
print(dsa.__version__)


### PARTE 1 == NUMPY ###

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




print("-"*50)