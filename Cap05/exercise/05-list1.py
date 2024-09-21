# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 5

### LISTA DE EXERCÍCIOS 1 ###
# Exercicios de Métodos e Funções

print("-"*50)
print("### Exercício 1 ###")
# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20
# (a função não recebe parâmetro) e depois faça uma chamada à função para listar os números

def um_lista_par():
    return [i for i in range(2, 21, 2)]

# Imprime o resultado da função
print(um_lista_par())


print("-"*50)
print("### Exercício 2 ###")
# Exercício 2 - Crie uma função que receba uma string como argumento e retorne a mesma string em
# letras maiúsculas. Faça uma chamada à função, passando como parâmetro uma string

def dois_string_up(texto):
    print(texto.upper())
    return

dois_string_up("Rumo à Análise de Dados")


print("-"*50)
print("### Exercício 3 ###")
# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos
# a lista e imprima a lista

def tres_novaLista(lista):
    lista.append(5)
    lista.append(6)
   
tres_lista1 = [1, 2, 3, 4]   
tres_novaLista(tres_lista1)
print(tres_lista1)


print("-"*50)
print("### Exercício 4 ###")
# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos.
# Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def tres_print_num( arg1, *lista ):
    print (arg1)
    for i in lista:
        print (i)
    return;

# Chamada à função
tres_print_num( 100 )
tres_print_num( "A", "B", "C" )


print("-"*50)
print("### Exercício 5 ###")
# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma.
# A expressão vai receber 2 números como parâmetro e retornar a soma deles

quatro_func = lambda arg1, arg2: arg1 + arg2

print ("A soma é: ", quatro_func( 452, 298 ))


print("-"*50)
print("### Exercício 6 ###")
# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local

total = 0
def seis_soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;

seis_soma( 10, 20 );
print ("Fora da função o total é: ", total)


print("-"*50)
print("### Exercício 7 ###")
# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
# Celsius = [39.2, 36.5, 37.3, 37.8]
# Fahrenheit = map(coloque_aqui_sua_função_lambda)
# print (list(Fahrenheit))

# Converter de grau Celsius para Fahrenheit: multiplicar a temperatura em graus Celsius por 1,8 e somar 32.

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print (list(Fahrenheit))


print("-"*50)
print("### Exercício 8 ###")
# Exercício 8 - Crie uma list comprehension que imprima o quadrado dos números de 1 a 10

oito_lista = [x**2 for x in range(1,11)]
print(oito_lista)


print("-"*50)
print("### Exercício 9 ###")
# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome

palavras = ["maça", "coiote", "banana", "terreno", "Python"]

nove_lista_a = [x for x in palavras if "a" in x]
print(nove_lista_a)


print("-"*50)
print("### Exercício 10 ###")
# Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um
# intervalo de 1 a 10

dez_lista = [x for x in range(1,11) if x < 5]
print(dez_lista)
