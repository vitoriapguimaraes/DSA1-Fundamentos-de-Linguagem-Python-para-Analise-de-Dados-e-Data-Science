# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 5

### PARTE 8 == LIST COMPREHENSION ###

### List Comprehension ###
#   [expressão for item in iterable if condição == True]

# List comprehension que imprime os números até 10
[x for x in range(10)]

# List comprehension que imprime os números até 10 e grava em uma lista Python
lista_numeros = [x for x in range(10)]

print(lista_numeros)


# List comprehension que imprime os números menores que 5 em um intervalo de 1 a 10
lista_numeros = [x for x in range(10) if x < 5]
print(lista_numeros)


# Lista de frutas
lista_frutas = ["banana", "abacate", "melancia", "cereja", "manga"]

# Nova lista
nova_lista = []

# Loop tradicional para buscar as palavras com letra "m"
for x in lista_frutas:
    if "m" in x:
        nova_lista.append(x)
# print(nova_lista)

# Mesmo resultado anterior mas com list comprehension
nova_lista = [x for x in lista_frutas if "m" in x]
print(nova_lista)


# Dict comprehension

# Dicionário de alunos e notas
dict_alunos = {"Bob": 68, "Michel": 84, "Zico": 57, "Ana": 93}

# Criamos um novo dicionário imprimindo os pares de chave:valor
dict_alunos_status = {k:v for (k, v) in dict_alunos.items()}
print(dict_alunos_status)


# Dict comprehension

# Dicionário de alunos e notas
dict_alunos = {'Bob': 68, 'Michel': 84, 'Zico': 57, 'Ana': 93}

# Criamos um novo dicionário com o status: nota maior que 70, aprovado, senão, reprovado
dict_alunos_status = {k:('Aprovado' if v > 70 else 'Reprovado') for (k, v) in dict_alunos.items()}
print(dict_alunos_status)


print("-"*50)