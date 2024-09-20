# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 4

### PARTE 4 == Estruturas de Dados (Listas) ###

### Trabalhando com Listas ###

lista_1 = ["arroz, frango, tomate, leite"]

print(type(lista_1))
print(lista_1)

lista_2 = ["arroz", "frango", "tomate", "leite"]

print(type(lista_2))
print(lista_2)

lista_3 = [23, 100, "Cientista de Dados"]

print(type(lista_3))
print(lista_3)

# Atribuindo cada valor da lista a uma variável

item1 = lista_3[0]
item2 = lista_3[1]
item3 = lista_3[2]

print(item1)
print(item2)
print(item3)

# Atualizando um Item da Lista

print(lista_2)

lista_2[2] = "chocolate"

print(lista_2)

# Deletando um Item da Lista

del lista_2[3]

print(lista_2)

### Listas de Listas (Listas Aninhadas) ###

listas = [ [1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3] ]

print(listas)

a = listas[0]
print(a)

b = a[0]
print(b)

list1 = listas[1]
print(list1)

valor_1_0 = list1[0]
print(valor_1_0)

list2 = listas[2]
print(list2)

valor_2_0 = list2[0]
print(valor_2_0)

### Operações com Listas ###

listas = [ [1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3] ]

a = listas[0][0]
print(a)

b = listas[1][2]
print(b)

c = listas[0][2] + 10
print(c)

d = 10
e = d * listas[2][0]
print(e)

### Concatenando Listas ###

lista_s1 = [34, 32, 56]
lista_s2 = [21, 90, 51]

lista_total = lista_s1 + lista_s2
print(lista_total)

### Operador in ###

lista_teste_op = [100, 2, -5, 3.4]

# Verificando se um valor pertence a lista
print(10 in lista_teste_op)
print(100 in lista_teste_op)

### Operador Built-in ###

numeros_lista = [10, 20, 50, -3.4]

# Comprimento da lista
print(len(numeros_lista))

# Maior valor dentro da lista
print(max(numeros_lista))

# Menos valor dentro da lista
print(min(numeros_lista))

formacoes_dsa_lista = ["Analista de Dados", "Cientista de Dados", "Engenheiro de Dados"]

print(formacoes_dsa_lista)

# Adicionar um item à lista
formacoes_dsa_lista.append("Engenheiro de IA")

print(formacoes_dsa_lista)

# Mais um append igual, "duplica" o mesmo item
formacoes_dsa_lista.append("Engenheiro de IA")

print(formacoes_dsa_lista)

# contabilizar quantas vezes um item aparece na lista
print(formacoes_dsa_lista.count("Engenheiro de IA"))

# Criando uma lista vazia

a = []
print(a)
print(type(a))

a.append(10)
print(a)

a.append(50)
print(a)


old_list = [1, 2, 5, 10]
new_list = []

print(old_list)
print(new_list)

# Copiando os itens de uma lista para outra (com loop)

for item in old_list:
    new_list.append(item)

print(new_list)


cidades = ["Recife", "Manaus", "Salvador"]
cidades.extend(["Fortaleza", "Palmas"])
print(cidades)

print(cidades.index("Salvador"))
print(cidades)

cidades.insert(2, 110)
print(cidades)

cidades.remove(110)
print(cidades)

cidades.reverse()
print(cidades)


# ordenar uma lista
x = [3, 2, 1, 4]

x.sort()
print(x)

print("-"*50)