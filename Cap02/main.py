# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 2

# pedi para o chatgpt: gere codigo python que crie uma lista com os numeros entre 1 a 100
# e então imprima os numeros pares, mas somente se o numero for divisivel por 4

# Gerando uma lista com os números de 1 a 100
numeros = list(range(1, 101))

# Filtrando e imprimindo apenas os números pares divisíveis por 4
for num in numeros:
    if num % 2 == 0 and num % 4 == 0:
        print(num)

print("-"*50)

# pedi para o chatgpt: gere codigo python que crie uma lista com os numeros entre 1 a 100
# e então imprima os numeros pares, mas somente se o numero for divisivel por 4,
# usando o list comprehension

# Gerando e imprimindo números pares divisíveis por 4 usando list comprehension
numeros_divisiveis_por_4 = [num for num in range(1, 101) if num % 2 == 0 and num % 4 == 0]

# Imprimindo os números
print(numeros_divisiveis_por_4)