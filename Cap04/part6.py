# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 4

### PARTE 6 == Estruturas de Dados (Tuplas) ###

### Trabalhando com Tuplas ###

# Criando uma tupla
tupla1 = ("Geografia", 23, "Elefantes", 9.8, "Python")
print(tupla1)

# Tuplas não suportam append(), delete, atribuição de item
# Tupla é uma estrutura IMUTÁVEL
# Tuplas podem ter um elemento único

# Slicing, da mesma forma que se faz com listas
print(tupla1[1:])

t2 = ("A", "B", "C")

# Usando a função lista() para converter uma tupla para lista

lista_t2 = list(t2)
print(type(t2))
print(type(lista_t2))

lista_t2.append("D")
print(lista_t2)

# Usando a função tuple() para converter uma lista para tupla
t2 = tuple(lista_t2)
print(t2)
print(type(t2))

print("-"*50)