# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 6

### PARTE 5 == FUNÇÃO REDUCE ###

### Função Reduce ###

# A função reduce() em Python é uma função da biblioteca functools que aplica uma determinada
# função binária a pares consecutivos de elementos em uma estrutura de dados iterável (como uma
# lista, tupla ou outro objeto iterável), reduzindo-a a um único valor.

# Importando a função reduce do módulo functools
from functools import reduce

# from PIL import Image
# # Abrir a imagem
# imagem = Image.open("Cap06/arquivos/reduce.png")
# # Exibir a imagem
# imagem.show()

# Criando uma lista
lista = [47, 11 , 42, 13]

print(lista)

# Função 
def soma(a,b):
    x = a + b
    return x

# Usando reduce com uma função e uma lista. A função vai retornar o valor máximo
lista_soma = reduce(soma, lista)

print(lista_soma)


# Criando uma lista
lst = [47, 11, 42, 13]

# Usando a função reduce() com lambda
print(reduce(lambda x,y: x+y, lst))

# Podemos atribuir a expressão lambda a uma variável
max_find2 = lambda a,b: a if (a > b) else b
print(type(max_find2))

# Reduzindo a lista até o valor máximo, através da função criada com a expressão lambda
print(reduce(max_find2, lst))

print("-"*50)