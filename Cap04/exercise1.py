# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 4

### LISTA DE EXERCÍCIOS ###


print("-"*50)
print("### Exercício 1 ###")
# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

ex1_lista = list(range(1,11))
print(ex1_lista)


print("-"*50)
print("### Exercício 2 ###")
# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

ex2_lista = ["computador", "monitor", "teclado", "mouse", "tablet"]
print(ex2_lista)


print("-"*50)
print("### Exercício 3 ###")
# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

a = "Eu sou "
b = "Vitória"
c = a + b

print(c)


print("-"*50)
print("### Exercício 4 ###")
# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e
# depois utilize a função count do objeto tupla para verificar quantas vezes o
# número 4 aparece na tupla

tupla_ex4 = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla_ex4.count(4))


print("-"*50)
print("### Exercício 5 ###")
# Exercício 5 - Crie um dicionário vazio e imprima na tela

dict_ex5 = {}
print(dict_ex5)


print("-"*50)
print("### Exercício 6 ###")
# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

dict_ex6 = {"Vitoria": 28, "João Bernardo": 29, "Tomas": 4}
print(dict_ex6)


print("-"*50)
print("### Exercício 7 ###")
# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior
# e imprima na tela

dict_ex6["Tereza"] = 7
print(dict_ex6)


print("-"*50)
print("### Exercício 8 ###")
# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dict_ex8 = {"k1": "teste", "k2": "aula", "k3": [2, 3]}
print(dict_ex8)


print("-"*50)
print("### Exercício 9 ###")
# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dicionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.

lista_ex9 = ["string 1", (1, "string 2"), {"inicio": 0, "fim": 10}, 3.14]
print(lista_ex9)

print(type(lista_ex9))

print(type(lista_ex9[0]))
print(type(lista_ex9[1]))
print(type(lista_ex9[2]))
print(type(lista_ex9[3]))


print("-"*50)
print("### Exercício 10 ###")
# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.

frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

print(frase[0:18])