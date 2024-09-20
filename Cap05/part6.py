# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 5

### PARTE 6 == FUNÇÕES ###

### Funções ###

print("Hello World")

# Definindo uma função
def primeiraFunc():
    print("Hello World")

primeiraFunc()


# Definindo uma função
def primeiraFunc():
    nome = "Bob"
    print(f"Hello {nome}")

primeiraFunc()

# Definindo uma função com parâmetro
def segundaFunc(nome):
    print(f"Hello {nome}")

segundaFunc("Aluno")


# Função para imprimir números
def imprimeNumeros():
    
    # Loop
    for i in range(0, 5):
        print("Número " + str(i))

imprimeNumeros()


# Função para somar números
def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
    print("Soma: ", firstnum + secondnum)

addNum(4, 7)

addNum(11, 21)


# Funções com número variável de argumentos
def printVarInfo( arg1, *vartuple ):
    
   # Imprimindo o valor do primeiro argumento
    print ("O parâmetro passado foi: ", arg1)
   
   # Imprimindo o valor do segundo argumento 
    for item in vartuple:
        print ("O parâmetro passado foi: ", item)
    return;

printVarInfo(10)

printVarInfo("Chocolate", "Morango")

printVarInfo("Data", "Science", "Academy")


### Escopo de Variável - Local e Global ###

# Variável Global
var_global = 10  # Esta é uma variável global

# Função
def multiplica_numeros(num1, num2):
    var_global = num1 * num2  # Esta é uma variável local
    print(var_global)

multiplica_numeros(3, 11)

print(var_global) # apesar do mesmo nome, não são a mesma. obs.: nomes iguais só para didática, não fazer isso na realidade

# def multiplica_numeros(num1, num2):
#     var_local = num1 * num2   # Esta é uma variável local
#     print(var_local)
# print(var_local) # variável só existe no def!


### Funções Built-in ###
# Não inventar a roda, buscar funções já criadas => documentação!

print(abs(-56))

print(bool(0))

print(int(3.56))

print(str(12))

print(float(7))


# idade = int(input("Digite sua idade: "))
# if idade > 13:
#     print("Você pode acessar Redes Sociais sem supervisão!")  
# else:
#     print("Seus pais não deveriam você acessar Redes Sociais sem supervisão!")  


print(len([23,34,45,46]))

array = [1, 2, 3]

print(max(array))

print(min(array))


list1 = [16, 23, 44, 75]

print(sum(list1))


### Criano Funções Usando Outras Funções ###

import math

# Verificando se um número é primo
def numPrimo(num):
    if (num % 2) == 0 and num > 2: 
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2): # sqrt == matriz quadrada
        if (num % i) == 0:
            return "Este número não é primo"
    return f"O número {num} é primo"

print(numPrimo(541))
print(numPrimo(4))


caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"

def lowercase(text):
    return text.lower()

lowercased_string = lowercase(caixa_baixa)

print(lowercased_string)


### Fazendo Split dos Dados ###

# Fazendo split dos dados
def split_string_palavras(text):
    return text.split(" ")

texto = "Esta função será bastante útil para separar grandes volumes de dados."

# Isso divide a string em uma lista de palavras
print(split_string_palavras(texto))

# Podemos atribuir o output de uma função para uma variável
token = split_string_palavras(texto)

print(token)


# Fazendo split dos dados
def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)

print(split_string_letras(texto))

print("-"*50)