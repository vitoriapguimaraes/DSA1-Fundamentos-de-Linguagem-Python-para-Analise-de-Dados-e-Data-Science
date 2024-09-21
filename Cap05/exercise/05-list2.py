# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 5

### LISTA DE EXERCÍCIOS 2 ###
# Exercícios de Loops e Condicionais


print("-"*50)
print("### Exercício 1 ###")
# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a
# Domingo ou igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na
# tela "Você precisa trabalhar!"

print("RESOLUÇÃO COMO COMENTÁRIO POR CAUSA DO INPUT, FACILITANDO O PROCESSO DA LISTA DE EXERCÍCIO")
# print("Informe o dia da semana: ")
# um_dia_usuario = input("Segunda / Terça / Quarta / Quinta / Sexta / Sábado / Domingo : ")
# um_dia_usuario = um_dia_usuario.lower()

# dia_trabalho = ["segunda", "terça", "quarta", "quinta", "sexta"]
# dia_descanso = ["sábado", "domingo"]

# if um_dia_usuario in dia_trabalho:
#     print(f"\nComo hoje é {um_dia_usuario}-feira, você precisa trabalhar!")
# elif um_dia_usuario in dia_descanso:
#     print(f"\nHoje é {um_dia_usuario}, um dia de descanso.")
# else:
#     print("Informação inválida")


print("-"*50)
print("### Exercício 2 ###")
# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

dois_lista = ["Morango", "Maça", "Melancia", "Kiwi", "Banana"]

x = "Morango"

if x in dois_lista:
    print(f"{x} pertence a lista.")
else:
    print(f"{x} não pertence a lista.")    


print("-"*50)
print("### Exercício 3 ###")
# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os
# resultados em uma lista

tres_tupla = (63, 2, 37, 3)
print(type(tres_tupla))

tres_lista = []

for i in tres_tupla:
    novo_valor = i * 2
    tres_lista.append(novo_valor)

print(tres_lista)
print(type(tres_lista))


print("-"*50)
print("### Exercício 4 ###")
# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

for quatro_i in range(100, 151, 2):
    print(quatro_i)


print("-"*50)
print("### Exercício 5 ###")
# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for
# maior que 35, imprima as temperaturas na tela

temperatura = 40

while temperatura > 35:
    print(temperatura)
    temperatura = temperatura - 1


print("-"*50)
print("### Exercício 6 ###")

# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os
# valores na tela, mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0

while contador < 100:
    print(contador)
    contador = contador + 1
    if contador == 23:
        break
    
    
print("-"*50)
print("### Exercício 7 ###")
# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou
# igual a 20, adicione à lista, apenas os valores pares e imprima a lista

sete_lista = []
sete_i = 4

while sete_i <= 20:
    sete_lista.append(sete_i)
    sete_i = sete_i + 2
print(sete_lista)


print("-"*50)
print("### Exercício 8 ###")
# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)

oito_nums = range(5, 45, 2)

print(list(oito_nums))


print("-"*50)
print("### Exercício 9 ###")
# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.

temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')


print("-"*50)
print("### Exercício 10 ###")

# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um
# placeholder na sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 

frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 

count = 0
for caracter in frase:
    if caracter == "r":
        count += 1
print(f"O caracter r aparece {count} vezes na frase.")