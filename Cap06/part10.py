# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 6

### LAB 3 ###

### PARTE 10 == Trabalhando com Expressões Regulares em Python com ChatGPT ###

### Expressões Regulares ###

# Expressões regulares são padrões usados para combinar ou encontrar ocorrências de sequências de
# caracteres em uma string. Em Python, expressões regulares são geralmente usadas para manipular
# strings e realizar tarefas como validação de entrada de dados, extração de informações de strings e
# substituição de texto.


import re

texto = "Meu e-mail é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com."

# Expressão regular para contar quantas vezes o caracter arroba aparece no texto
resultado = len(re.findall("@", texto))

print("O caractere '@' apareceu", resultado, "vezes no texto.")


# Expressão regular para extrair a palavra que aparece após a palavra "você" em um texto
resultado = re.findall(r"você (\w+)", texto)

print("A palavra após 'você' é:", resultado[0])

# Nota: O r antes da string que representa a expressão regular em Python é usado para indicar que a
# string é uma string literal raw. Isso significa que as barras invertidas (\) não são interpretadas
# como caracteres de escape, mas são incluídas na expressão regular como parte do padrão.


# Expressão regular para extrair endereços de e-mail de uma string
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
                        # padrão para achar email. documentação + chatgpt

print(emails)

# Visite sua amiga, a documentação: https://docs.python.org/3.9/library/re.html

text = "O aluno estava incrivelmente perdido, mas encontrou a DSA e rapidamente começou a aprender."

# Extraindo os advérbios da frase
for m in re.finditer(r"\w+mente\b", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))


### REGEX com ChatGPT ###

# Variável do tipo string
musica = '''
Todos os dias quando acordo
Não tenho mais
O tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço
Como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo
Que esse sangue amargo
E tão sério
E selvagem! Selvagem!
Selvagem!
Veja o sol
Dessa manhã tão cinza
A tempestade que chega
É da cor dos teus olhos
Castanhos
Então me abraça forte
E diz mais uma vez
Que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens! Tão jovens!
'''

print(musica)

    # REGEX = expressão regular
    
## Criar esses REGEX com ajuda do ChatGPT

# 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.
# 2- Crie um REGEX em Python para contar quantas vezes a palavra "tempo" aparece na música.
# 3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.
# 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e o sucessor seja a palavra "amargo" em um texto.
# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento.


# ChatGPT: 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.
ocorrencias_a = re.findall(r"a", musica)
quantidade_a = len(ocorrencias_a)
print(f"O caractere 'a' aparece {quantidade_a} vezes na música.")

# 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.
resultado1 = len(re.findall("a", musica))
print("O caractere 'a' apareceu", resultado1, "vezes na música.")


# ChatGPT: 2- Crie um REGEX em Python para contar quantas vezes a palavra "tempo" aparece na música.
ocorrencias_tempo = re.findall(r'\btempo\b', musica)
quantidade_tempo = len(ocorrencias_tempo)
print(f"A palavra 'tempo' aparece {quantidade_tempo} vezes na música.")

# 2- Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música.
resultado2 = len(re.findall("tempo", musica))
print("A palavra 'tempo' apareceu", resultado2, "vezes na música.")


# ChatGPT: 3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.
palavras_com_exclamacao = re.findall(r'\b\w+!\b', musica)
print("As palavras seguidas por exclamação são:", palavras_com_exclamacao)

# 3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.
resultado3 = re.findall(r'\b\w+!', musica)
print("Estas são as palavras seguidas por exclamação:", resultado3)


# ChatGPT: # 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e
# o sucessor seja a palavra "amargo" em um texto.
palavras_entre_esse_e_amargo = re.findall(r'\besse\s+(\w+)\s+amargo\b', musica)
print("Palavras entre 'esse' e 'amargo':", palavras_entre_esse_e_amargo)

# 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e 
# o sucessor seja a palavra "amargo" em um texto.
resultado4 = re.findall(r'\besse\s(\w+)\samargo\b', musica)
print("Palavra(s) encontrada(s):", resultado4)


# ChatGPT: 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são
# anteriores ao caracter com acento.
palavras_antes_do_acento = re.findall(r'\b(\w*?)[áéíóúâêîôûãõç]\w*\b', musica)
print("Partes das palavras com acentos:", palavras_antes_do_acento)

# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são
# anteriores ao caracter com acento.
resultado5 = re.findall(r'\b[\wÀ-ÿ]+[áéíóúãõç]', musica)
print("As palavras acentuadas são:", resultado5)


print("-"*50)