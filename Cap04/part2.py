# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 4

### PARTE 2 == Variáveis e Operadores em Python ###

### Trabalhando com Variáveis ###

var_teste = 9.5
print(var_teste)
print(type(var_teste))

x = 1
print(x)

### Declaração Múltipla ###

pessoa1, pessoa2, pessoa3 = "Bob", "Maria", "Ana"

print(pessoa1)
print(pessoa2)
print(pessoa3)

fruta1 = fruta2 = fruta3 = "Melancia"

print(fruta1)
print(fruta2)
print(fruta3)

### Variáveis Atribuídas a Outras Variáveis e Ordem dos Operadores ###

largura = 2
altura = 4
area = largura * altura
print(area)

perimetro = 2 * largura + 2 * altura
print(perimetro)

### Operações com Variáveis ###

idade1 = 25
idade2 = 35

print(idade1 + idade2)
print(idade1 - idade2)
print(idade1 * idade2)
print(idade1 / idade2)
print(idade1 % idade2)

### Concatenação de Variáveis ###

nome = "Bob"
sobrenome = "Marley"
full_name = nome + " " + sobrenome
print(full_name)
full_name = nome, sobrenome
print(full_name)

print("-"*50)