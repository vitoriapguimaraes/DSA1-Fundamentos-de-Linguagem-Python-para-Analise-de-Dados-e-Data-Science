# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 6

### PARTE 6 == FUNÇÃO FILTER ###

### Função Filter ###

# A função filter() em Python é uma função que filtra elementos de uma estrutura de dados iterável
# (como uma lista, tupla ou outro objeto iterável) com base em uma determinada condição. A função
# filter() retorna um objeto filtro, que pode ser convertido em outra estrutura de dados, como uma
# lista, se necessário.


# Criando uma função
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Chamando a função e passando um número como parâmetro. Retornará 
# Falso de for ímpar e True se for par.
print(verificaPar(35))
print(verificaPar(10))


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

# A função filter() retorna um iterator
filter(verificaPar, lista)

print(list(filter(verificaPar, lista)))

print(list(filter(lambda x: x%2==0, lista)))

print(list(filter(lambda num: num > 8, lista)))

print("-"*50)