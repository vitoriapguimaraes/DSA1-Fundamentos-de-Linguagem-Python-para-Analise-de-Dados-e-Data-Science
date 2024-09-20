# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 5

### PARTE 3 == TRABALHANDO COM LOOP WHILE FOR EM PYTHON ###

### Loop While ###

# Usando o loop while para imprimir os valores de 0 a 9
# A condição tem que deixar de ser verdadeira dentro do loop, senão pode travar o navegador ou mesmo o computador
valor = 0
while valor < 10:
    print(valor)
    valor = valor + 1

# Entra no loop somente se a condição for verdadeira
valor = 11
while valor < 10:
    print(valor)
    valor = valor + 1

# Também é possível usar a claúsula else para encerrar o loop while
x = 0

while x < 10:
    print ('O valor de x nesta iteração é: ', x)
    print (' x ainda é menor que 10, somando 1 a x')
    x += 1 
else:
    print ('Loop concluído!')
print(x)


### Pass, Break, Continue ###

# Se encontramos o número 4 interrompemos o loop
valor = 0
while valor < 10:
    if valor == 4:
        break
    else:
        pass
    print(valor)
    valor = valor + 1

# Desconsideramos a letra z ao imprimir os caracteres da frase
for letra in "Python é zzz incrível!":
    if letra == "z":
        continue
    print(letra)

print("-"*50)