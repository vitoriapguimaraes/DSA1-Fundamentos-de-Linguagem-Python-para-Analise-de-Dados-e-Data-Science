# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 7

### INTRODUÇÃO À PROGRAMAÇÃO ORIENTADA A OBJETOS ###

### PARTE 4 == Trabalhando com Herança de Classes em Python ###

# Em Programação Orientada a Objetos (POO), a herança é um conceito que permite criar novas classes a
# partir de outras classes existentes, aproveitando os atributos e métodos da classe original e
# adicionando novos atributos e métodos específicos. 
# 
# A classe original é chamada de classe mãe ou superclasse e a nova classe criada é chamada de classe
# filha ou subclasse.
# 
# A herança é uma técnica importante em POO porque permite reutilizar o código de maneira eficiente.
# Em vez de criar uma nova classe do zero, a subclasse pode herdar todos os atributos e métodos da
# superclasse e adicionar apenas o que é necessário. Dessa forma, a subclasse pode se concentrar em
# fornecer funcionalidades adicionais sem precisar se preocupar com as características básicas da classe.
# 
# Na herança, uma subclasse pode herdar os atributos e métodos da superclasse e substituí-los ou
# estendê-los conforme necessário. Por exemplo, uma subclasse pode ter um método com o mesmo nome de um
# método da superclasse, mas com um comportamento diferente. 


# Criando a classe Animal - Super-classe
class Animal:
    
    def __init__(self):
        print("Animal criado.")

    def imprimir(self):
        print("Este é um animal.")

    def comer(self):
        print("Hora de comer.")
        
    def emitir_som(self):
        pass


# Criando a classe Cachorro - Sub-classe
class Cachorro(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado.")
    
    def emitir_som(self):
        print("Au au!")


# Criando a classe Gato - Sub-classe
class Gato(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado.")
    
    def emitir_som(self):
        print("Miau!")


# Criando um objeto (Instanciando a classe)
rex = Cachorro()

# Criando um objeto (Instanciando a classe)
zeze = Gato()


rex.emitir_som() 

zeze.emitir_som() 


# Executando o método da classe Cachorro (sub-classe)
rex.imprimir()


# Executando o método da classe Animal (super-classe)
rex.comer()

# Executando o método da classe Cachorro (sub-classe)
zeze.comer()

print("-"*50)