# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

#####################################################################
# Selecione o número da operação desejada:                          #
#     1 - Soma                                                      #
#     2 - Subtração                                                 #
#     3 - Multiplicação                                             #
#     4 - Divisão                                                   #
# Digite sua opção (1, 2, 3, 4):                                    #
# Digite o primeiro número:                                         #
# Digite o segundo número:                                          #
# Operação = resultado                                              #
#####################################################################

operacao = int(input("Selecione o número da operação desejada: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n"))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == 1:
    resultado = num1 + num2
    texto_operador = "+"
    print(f"{num1} {texto_operador} {num2} = {resultado}")
# elif