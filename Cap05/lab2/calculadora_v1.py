# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

#####################################################################
# Selecione o número da operação desejada:                          #
#     1 - Soma                                                      #
#     2 - Subtração                                                 #
#     3 - Multiplicação                                             #
#     4 - Divisão                                                   #
# Digite sua opção (1, 2, 3, 4):                                    #
# Digite o primeiro número:                                         #
# Digite o segundo número:                                          #
#####################################################################

import sys

print("\n******************* Calculadora em Python *******************")

### Condições básicas de funcionamento ###

operacao = input("Selecione o número da operação desejada: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n")
op_possiveis = ["1", "2", "3", "4"]

if operacao not in op_possiveis:
    print("O campo não foi preenchido corretamente.")
    sys.exit()  # Para a execução do programa
operacao = float(operacao)


def verificar_numero(entrada):
    try:
        entrada = float(entrada)  # Tenta converter para número (aceita inteiros e decimais)
    except ValueError:
        print("O campo não foi preenchido corretamente.")
        sys.exit()  # Para a execução do programa

num1 = input("Digite o primeiro número: ")
verificar_numero(num1)
num1 = float(num1)

num2 = input("Digite o segundo número: ")
verificar_numero(num2)
num2 = float(num2)

print("-"*50)

### Cálculos das operações ###

if operacao == 1:
    resultado = num1 + num2
    texto_operador = "+"
    print(f"{num1} {texto_operador} {num2} = {resultado}")
    
elif operacao == 2:
    resultado = num1 - num2
    texto_operador = "-"
    print(f"{num1} {texto_operador} {num2} = {resultado}")
    
elif operacao == 3:
    resultado = num1 * num2
    texto_operador = "*"
    print(f"{num1} {texto_operador} {num2} = {resultado:.3f}")

elif operacao ==4:
    if num2 == 0:
        print("Não é possível fazer essa operação.")
    else:
        resultado = num1 / num2
        texto_operador = "/"
        print(f"{num1} {texto_operador} {num2} = {resultado:.3f}")

print("-"*50)


### Tempo de execução ###

import timeit
tempo_execucao = timeit.timeit('sum(range(1000))', number=10000)
print(f"Tempo de execução: {tempo_execucao:.3f} segundos")