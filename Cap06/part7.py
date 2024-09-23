# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 6

### PARTE 7 == FUNÇÃO ZIP ###

### Função Zip ###

# A função zip() em Python é uma função que agrupa elementos de múltiplas estruturas de dados
# iteráveis (como listas, tuplas ou outros objetos iteráveis) juntos em pares. A função zip()
# retorna um objeto zip, que pode ser convertido em outra estrutura de dados, como uma lista ou
# dicionário, se necessário.


# Criando duas listas
x = [1,2,3]
y = [4,5,6]

# Unindo as listas. Em Python3 retorna um iterator
print(zip(x, y))

# Perceba que zip retorna tuplas. Neste caso, uma lista de tuplas
print(list(zip(x,y)))


# Atenção quando as sequências tiverem número diferente de elementos
print(list(zip('ABCD', 'xy')))              # ele cria a combinação! descarta itens adicionais

# Criando duas listas
a = [1,2,3]
b = [4,5,6,7,8]

print(list(zip(a,b)))


# Criando 2 dicionários
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

# Zip vai unir as chaves
print(list(zip(d1,d2)))

# Zip pode unir os valores (itens)
print(list(zip(d1, d2.values())))
print(list(zip(d1.values(), d2.values())))


# Criando uma função para trocar valores entre 2 dicionários
def trocaValores(d1, d2):
    
    dicTemp = {}
    
    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val
    
    return dicTemp

print(trocaValores(d1, d2))

print("-"*50)