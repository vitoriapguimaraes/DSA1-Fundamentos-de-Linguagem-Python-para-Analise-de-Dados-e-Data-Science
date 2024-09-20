# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 5

### PARTE 1 == Estruturas de repetição, estruturas condicionais e funções ###

### Condicional If ###

if 5 > 2:
    print("A sentença é verdadeira!")

if 5 < 2:
    print("A sentença é verdadeira!")
else:
        print("A sentença é falsa!")

dia = "Terça"

if dia == "Segunda":
    print("Hoje fará sol.")
else:
    print("Hoje vai chover!")

dia = "Quarta"

if dia == "Segunda":
    print("Hoje fará sol.")
elif dia == "Terça":
    print("Hoje vai chover!")
else:
    print("Sem previsão do tempo para o dia selecionado.")


### Condicionais Aninhados ###

idade = 18
if idade > 17:
    print("Você pode dirigir.")

nome = "Bob"
if idade > 13:
    if nome == "Bob":
        print("Ok, Bob, você está autoprozado a entrar!")
    else:
        print("Desculpe, Bob, mas você não pode entrar.")

idade = 13
nome = "Bob"
if idade >= 13 and nome == "Bob":
    print("Ok, Bob, você está autoprozado a entrar!")

idade = 11
nome = "Bob"
if (idade >= 13) or (nome == "Bob"): # parênteses nas condições para facilitar visualização
    print("Ok, Bob, você está autoprozado a entrar!")


### Operações Lógicas ###
# operador **and** == retorna True se ambas as declarações forem verdadeiras
# operador **or** == retorna True se uma das declarações for verdadeira
# operador **not** = inverte o resiltado, retorna False se o resultado for True

num = 4

# operador **and**
if num > 5 and num % 2 == 0:
    print("Isso está sendo impresso porque as duas condições são verdadeiras.")
else:
    print("Isso está sendo impresso porque uma das duas condições é falsa.")

# operador **or**
if num > 5 or num % 2 == 0:
    print("Isso está sendo impresso porque uma das duas condições é verdadeira.")
else:
    print("Isso está sendo impresso porque nenhuma das condições é verdadeira.")

# operador **not** 
if not num > 5 and num % 2 == 0:
    print("Isso está sendo impresso porque as duas condições são verdadeira.")
else:
    print("Isso está sendo impresso porque uma das duas condições é falsa.")

# operador anda, or e not
if (not(num > 5) and (num % 2 == 0)) or (num == 4):
    print("Isso está sendo impresso porque as duas primeiras condições são verdadeiras ou a terceira é verdadeira!")

# Exemplo com o uso de variáveis

disciplina = "Data Science"
nota_final = 70

if disciplina == "Data Science" and nota_final >= 70:
    print("Você foi aprovado!")
else:
    print("Lamento, acho que você precisa estudar mais!")

# Usando mais de uma condição na cláusula if e introduzindo Placeholders

disciplina = "Data Science"
nota_final = 90
semestre = 2

if disciplina == "Data Science" and nota_final >= 80 and semestre != 1:
    print("Você foi aprovado em %s com média final %r!" %(disciplina, nota_final))
else:
    print("Lamento, acho que você precisa estudar mais!")

# prefiro assim:
if disciplina == "Data Science" and nota_final >= 80 and semestre != 1:
    print(f"Você foi aprovado em {disciplina} com média final {nota_final}!")
else:
    print("Lamento, acho que você precisa estudar mais!")

print("-"*50)