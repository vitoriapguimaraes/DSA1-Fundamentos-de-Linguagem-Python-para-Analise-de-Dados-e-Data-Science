# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 3

# PSEUDOCÓDIGO 1 - Calcular a área dee uum paralelograma

# Inicie
#   Exiba 'Bem-vindo ao Calculador de Área de Paralelograma'
#   Peça para o usuário inserir o comprimento da base
#   Armazene o comprimento da base em uma variável
#   Peça para o usuário inserir a altura
#   Armazene a altura em uma variável
#   Calcule a área do paralelograma: base * altura
#   Armazene o resultado em uma variável
#   Exiba o resultado
# Fim

print("Bem-vindo ao Calculador de Área de Paralelograma")
base = float(input("Insira o comprimento da base (em cm): "))
altura = float(input("Insira a altura (em cm): "))
area = base * altura
print(f"A área do paralelograma é {area} cm\u00B2")

print("-"*50)

# PSEUDOCÓDIGO 2 - Calculadora simples

# Inicie
#   Exiba 'Bem-vindo a Calculadora'
#   Peça para o usuário inserir o primeiro valor
#   Armazene o primeiro valor em uma variável
#   Peça para o usuário inserir o segundo valor
#   Armazene o segundo valor em uma variável
#   Peça para o usuário selecionar uma operação (+, -, *, /)
#   Armazene a operação em uma variável
#   Utilize a operação selecionada e os números armazenados para realizar o cálculo
#   Exiba o resultado
# Fim

print("Bem-vindo a Calculadora")


num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))

operacao = input("Selecionar uma operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado da operação {num1} {operacao} {num2} = {resultado}.")

elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado da operação {num1} {operacao} {num2} = {resultado}.")

elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado da operação {num1} {operacao} {num2} = {resultado}.")

elif operacao == "/":
    resultado = num1 / num2
    print(f"O resultado da operação {num1} {operacao} {num2} = {resultado}.")

else:
    print("Operação inválida.")
    
print("-"*50)

# PSEUDOCÓDIGO 3 - Algoritmo Bubble Sort
# Bubble Sort é um algoritmo de ordenação simples que funiona comparando cada elemento com o próximo, e trocando-os de lugar
# se eles estiverem em ordem incorreta. O algoritmo repete esse processo várias vezes até que todos os elementos estejam
# ordenados. A cada passagem, o maior elemento "flutua" para o final do array, como uma bolha, dando origem ao nome do algoritmo.
# obs.: o bubble sort não é o melhor para fazer isso, mas é o mais didático para iniciante

# Inicie
#   Para cada elemento i no array de tamanho n
#       Para cada elemento j no array de tamanho n - 1
#           Se elemento i for maior que elemento j
#               Troque os elementos i e j
#   Exiba o array ordenado
# Fim

lista = [6, 7, 19, 3, 5, 10, 11, 79, 36, 222, 23, 32, 44, 85]

def bubble_sort(arr):
    
    n = len(arr)
    
    # Para cada elemento i do array
    for i in range(n):
        
        # Para cada elemento j do array
        for j in range(0, n-i-1):
            
            # Se elemento i for maior que elemento j
            if arr[j] > arr[j+1]:
                
                # Troque os elementos i e j
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

print(bubble_sort(lista))

lista2 = [6, 7, 19, 3, 5, 10, 11, 79, 36, 222, 23, 32, 44, 85, 57, 33, 15, 17, 348, 683, 1000, 1]
print(bubble_sort(lista2))