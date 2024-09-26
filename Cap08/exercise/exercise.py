# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 08

### LISTA DE EXERCÍCIOS 01 ###


print("-"*50)
print("### Exercício 1 ###")
# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, 
# passando 2 parâmetros e depois faça uma chamada aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        
roc1 = Rocket(1, 3)
roc1.print_rocket()

roc1.move_rocket(4, 10)
roc1.print_rocket()


print("-"*50)
print("### Exercício 2 ###")
# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo
# menos 2 métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos
# um dos seus métodos # especiais.

class Pessoa():
    
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
    
    def detalhe_pessoa(self):
        print(f"As informações de {self.nome}, localizado em {self.cidade}, foi salvo.")
        print(f"O contato pode ser feito atras do telefone {self.telefone} ou por email: {self.email}")

teste1 = Pessoa("Fulano", "São Paulo", "11997111111", "fulano@email.com")

teste1.detalhe_pessoa()

print("-"*50)
print("### Exercício 3 ###")
# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():
    
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

class MP3Player(Smartphone):
    
    def __init__(self, capacidade, tamanho = 'Pequeno', interface = 'Android'):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)

    def print_produto(self):
        print(f"O MP3Player é {self.tamanho.lower()} e tem interface {self.interface}.")
        print(f"O MP3Player tem capacidade de {self.capacidade} GB.")

teste2 = MP3Player ("128")
teste2.print_produto()

print("-"*50)