# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 6

### PARTE 1 == MANIPULAÇÃO DE ARQUIVOS, parte 2 ###

### Manipulação Arquivos TXT ###

# TXT é a extensão de arquivo para arquivos de texto puro. Um arquivo TXT é um arquivo de texto
# simples sem formatação, como negrito, itálico ou fontes diferentes. Ele pode ser aberto e
# editado com muitos aplicativos diferentes, incluindo editores de texto, processadores de texto
# e IDEs. Arquivos TXT são amplamente utilizados para armazenar dados de texto simples, como
# listas, notas e documentos de texto. Eles são universais e podem ser lidos em praticamente
# qualquer dispositivo ou sistema operacional.

texto = "Cientista de Dados pode ser uma excelente alternativa de carreira.\n"
texto = texto + "Esses profissionais precisam saber como programar em Python.\n"
texto += "E, claro, devem ser proficientes em Data Science."

print(texto)


# Importando o módulo os
import os

# Criando um arquivo 
arquivo = open(os.path.join("Cap06/arquivos/cientista.txt"),"w")

# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + " ")

# Fechando o arquivo
arquivo.close()

# Lendo o arquivo
arquivo = open("Cap06/arquivos/cientista.txt","r")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)


### Usando a Expressão WITH ###


print("-"*50)