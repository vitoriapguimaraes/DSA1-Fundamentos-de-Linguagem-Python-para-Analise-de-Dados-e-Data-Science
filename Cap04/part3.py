# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 4

### PARTE 3 == Strings e Indexação ###

### Criando  e Imprimindo uma String ###

print("Podemos usar aspas duplas ou simples para strings em Phyton")

print("Testando \n strings \n em Phyton")

print("\n")

### Indexando Strings ###

s = "Data Science Academy"

print(s)

    # Indexação em Python começa por zero.

print(s[0])

print(s[1])

print(s[2])

print(s[3])

print(s[4])

print(s[5])

# Retorna todos os elementos da string, começando pela posição até o fim da string

print(s[1:])
print(s[:3])
print(s[-1])
print(s[:-1])

print(s[::2])

print(s[::-1])

print(s) # Indexação não altera a variável

### Propriedades de Strings ###

# Alterando um caracter (não é possível alterar um elemento da string)
# s[0] = "x" # erro

# Concatenando strings
print(s + " é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dado!")

letra = "w"

print(letra * 3)

### Funções Bulit-in de Strings ###

# Upper Case

# Upper Case
s = s.upper()
print(s)

# Lower Case
s = s.lower()
print(s)

# dividir uma string por espaços em branco (padrão)
s = s.split()
print(s)

s = "Data Science Academy"

s = s.split("y")
print(s)

### Funções String ###

s = "Data Science Academy"

s = s.capitalize()
print(s)

s = s.count("a")
print(s)

s = "Data Science Academy"

s = s.isalnum()
print(s)

s = "Data Science Academy"

s = s.islower()
print(s)

s = "Data Science Academy"

s = s.isspace()
print(s)

s = "Data Science Academy"

s = s.endswith("Y")
print(s)

### Comparando String ###

print("Python" == "R")

print("Python" == "Python")

print("-"*50)