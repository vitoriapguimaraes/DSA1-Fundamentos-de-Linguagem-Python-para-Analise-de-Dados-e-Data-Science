# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 5

### PARTE 4 == INTERVALOS DE VALORES ###

### Função Range ###

# Imprimindo números de 1 a10
for i in range(1, 11):
    print(i)

# Imprimindo números pares entre 50 e 101
for i in range(50, 101, 2):
    print(i)

# Imprimindo os números pares negativos entre 0 e -20
for i in range(0, -20, -2):
    print(i)

# Usando o tamanho de uma lista na função range()
lista = ['Abacaxi', 'Banana', 'Morango', 'Uva']
lista_tamanho = len(lista)
for i in range(0, lista_tamanho):
    print(lista[i])

print("-"*50)