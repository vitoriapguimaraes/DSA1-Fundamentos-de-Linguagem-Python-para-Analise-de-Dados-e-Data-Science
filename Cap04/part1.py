# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 4

### PARTE 1 == Números e Operações Matemáticas ###

### Operações básicas ###

# Soma "+"
print(4 + 3)

# Subtração "-"
print(4 - 3)

# Multiplicação "*"
print(4 * 3)

# Divisão "/"
print(1 / 4)

# Potência "**"
print(4 ** 3)

# Módulo "%"
print(10 % 3)

# Função type
print(type(5))
print(type(5.0))
a = "Estou estudando na Data Sciencia Academy"
print(type(a))

### Operações com Números Float ###

# Soma de float == float
a = 3.1 + 6.4
print(a)
print(type(a))

# Soma de float + inteiro == float
a = 3.1 + 2
print(a)
print(type(a))

# Soma de inteiro == inteiro
a = 4 + 2
print(a)
print(type(a))

# Divisão de inteiro com "/" == float
a = 4 / 2
print(a)
print(type(a))
a = 4 / 3
print(a)
print(type(a))

# Divisão de inteiro com "//" == inteiro
a = 4 // 2
print(a)
print(type(a))
a = 4 // 3
print(a)
print(type(a))

# Divisão de inteiro e float com "//" == inteiro
a = 4 // 3.0
print(a)
print(type(a))

### Conversões ###

num = 9
conversao = float(num)
print(conversao)
print(type(conversao))

num = 6.0
conversao = int(num)
print(conversao)
print(type(conversao))

num = 6.7
conversao = int(num)
print(conversao)
print(type(conversao))

### Hexadecimal e Binário ###

print(hex(394))

print(bin(394))

### Funções abs, round e pow ###

# Retorna o valor absoluto
print(abs(-8))
print(abs(8))

# Retorna o valor com duas casas decimais
print(round(3.14151922, 2))

# Potência
print(pow(4,2))

print("-"*50)