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






print("-"*50)