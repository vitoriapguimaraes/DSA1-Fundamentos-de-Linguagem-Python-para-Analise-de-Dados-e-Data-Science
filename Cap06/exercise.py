# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 06

### LISTA DE EXERCÍCIOS 01 ###


print("-"*50)
print("### Exercício 1 ###")
# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

um_lista = [1, 2, 3]
um_pot_tres = [num**3 for num in um_lista]
print(um_pot_tres)


print("-"*50)
print("### Exercício 2 ###")
# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!

palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()

resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)

# map
dois_map = map(lambda w:[w.upper(), w.lower(), len(w)], palavras)
for i in dois_map:
    print(i)


print("-"*50)
print("### Exercício 3 ###")
# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link:
# https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de
# sistemas de IA.
matriz = [[1, 2],[3,4],[5,6],[7,8]]

tres_matriz_transposta = [[linha[i] for linha in matriz] for i in range(len(matriz[0]))]
print(tres_matriz_transposta)


print("-"*50)
print("### Exercício 4 ###")
# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

def quadrado(x):
    return x**2

def cubo(x):
    return x**3

potencias = [quadrado, cubo]

for i in lista:
    valor = map(lambda x: x(i), potencias)
    print(list(valor))

    
print("-"*50)
print("### Exercício 5 ###")
# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]

cinco_resultado = list(map(pow, listaA, listaB))
print(cinco_resultado)


print("-"*50)
print("### Exercício 6 ###")
# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar 
# apenas os valores negativos.
range(-5, 5)

print(list(filter(lambda x:x<0, range(-5, 5))))


print("-"*50)
print("### Exercício 7 ###")
# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

print(list(filter(lambda x: x in a, b)))


print("-"*50)
print("### Exercício 8 ###")
# Exercício 8 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

print(dict(zip(dict1, dict2.values())))

# do gabarito
def trocaValores(d1, d2):
    dicTemp = {}
    for d1key, d2val in zip(d1,d2.values()):
        dicTemp[d1key] = d2val
    return dicTemp
dict3 = trocaValores(dict1, dict2)
print(dict3)


print("-"*50)
print("### Exercício 9 ###")
# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# print(list(enumerate(lista)))

for indice, valor in enumerate(lista):
    if indice <= 5:
        continue
    else:
        print(valor)


print("-"*50)
print("### Exercício 10 ###")
# Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras 
# "Data" e "Science" na frase: 'A Data Science Academy oferce os melhores cursos de análise de
# dados do Brasil.'

import re

texto = "A Data Science Academy oferece os melhores cursos de análise de dados do Brasil."

padrao = r"Data Science\s+(\w+)"
resultados = re.findall(padrao, texto)
print(resultados)

# gabarito
resultado = re.findall(r'Data Science (\w+)', texto)
print("A palavra após 'Data Science' é:", resultado[0])