# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 7

### INTRODUÇÃO À PROGRAMAÇÃO ORIENTADA A OBJETOS ###

### PARTE 3 == Trabalhando com Métodos de Classes em Python ###

# Em Python, os métodos de classes são funções definidas dentro de uma classe, que realizam operações
# específicas em objetos criados a partir dessa classe. Os métodos de classes são usados para implementar
# o comportamento dos objetos que pertencem a essa classe.
# 
# Assim como as funções em Python, os métodos de classes podem receber argumentos e retornar valores.
# No entanto, diferentemente das funções normais, os métodos de classes sempre incluem o parâmetro self
# como o primeiro argumento, que é usado para se referir ao objeto atual da classe.

# O método __init__ é um método especial que é chamado quando um objeto é criado a partir da classe.
# Este método é usado para inicializar os atributos do objeto. Outros métodos podem ser definidos para
# executar tarefas específicas em um objeto, como calcular valores, realizar operações de entrada e saída,
# ou alterar o estado do objeto.


# Criando uma classe chamada Circulo
class Circulo():
    
    # O valor de pi é constante
    pi = 3.14

    # Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5.
    def __init__(self, raio = 5):
        self.raio = raio

    # Esse método calcula a área. 
    def area(self):
        return (self.raio * self.raio) * Circulo.pi

    # Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    # Método para obter o raio do círculo
    def getRaio(self):
        return self.raio

# Criando o objeto circ, uma instância da classe Circulo()
circ = Circulo()

# Executando um método da classe Circulo
print(circ.getRaio())


# Criando outro objeto chamado circ1. Uma instância da classe Circulo()
# Agora sobrescrevendo o valor do atributo
circ1 = Circulo(7)

# Executando um método da classe Circulo
print(circ1.getRaio())

# Imprimindo o raio
print ('O raio é:', circ.getRaio())
# Imprimindo a area
print('Área igual a:', circ.area())

# Gerando um novo valor para o raio do círculo
circ.setRaio(3)
# Imprimindo o novo raio
print ('Novo raio igual a:', circ.getRaio())

print("-"*50)