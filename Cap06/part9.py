# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 6

### PARTE 9 == TRATAMNTO DE ERROS E EXCEÇÕES ###

### Erros e Exceções ###

# Sempre leia as mensagens de erro. Erros fazem parte do processo de aprendizagem e vão acompanhar
# você na sua jornada em programação, em qualquer linguagem.

# Erro (leia a mensagem de erro)
# print("Hello)
# SyntaxError: unterminated string literal (detected at line 11)
print("Hello")


# Erro (leia a mensagem de erro)
# 8 + "s"
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# Criando uma função
def numDiv (num1, num2):
    resultado = num1 / num2
    print(resultado)

# Execução não gera erro
numDiv(4,2)

# Execução gerando erro (leia a mensagem de erro)
# numDiv(4,0)


### Try, Except, Finally ###

# 8 + "s"
# Utilizando try e except
try:
    8 + "s"
except TypeError:
    print("Operação não permitida")

# Utilizando try, except e else
try:
    f = open("Cap06/arquivos/testandoerros.txt","w")
    f.write("Gravando no arquivo")
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()


# Utilizando try, except e else
try:
    f = open("Cap06/arquivos/testandoerros","r")
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser lido.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()


# Utilizando try, except, else e finally
try:
    f = open("Cap06/arquivos/testandoerros.txt","w")
    f.write("Gravando no arquivo")
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()
finally:
    print ("Comandos no bloco finally são sempre executados!")


# Cada possibilidade de erro deve ser tratada no seu programa.

def askint():
    try:
        val = int((input("Digite um número: ")))
    except:
        print ("Você não digitou um número!")
    finally:
        print ("Obrigado!")
    print(val)
# askint()

def askint():
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            val = int(input("Tente novamente. Digite um número: "))
        finally:
            print ("Obrigado!")
        print (val) 
# askint()

def askint():
    while True:
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            continue
        else:
            print ("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
    print (val)
askint()


# Uma lista completa de exceções em Python pode ser encontrada aqui:
# https://docs.python.org/3.9/library/exceptions.html


print("-"*50)