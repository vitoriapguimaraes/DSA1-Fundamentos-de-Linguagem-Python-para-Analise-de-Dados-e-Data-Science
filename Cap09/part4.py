# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 9

### Python para Análise de Dados, Ciência de Dados, Machine Learning e Inteligência Artificial == Pacote NumPy ###

# Importando o NumPy
import numpy as dsa


### Análise Estatística Básica com NumPy ###

# Criando um array
arr14 = dsa.array([15, 23, 63, 94, 75])

# Em Estatística, a média é uma medida de tendência central que representa o valor central de um conjunto de
# dados. É calculada somando-se todos os valores do conjunto de dados e dividindo-se pelo número de observações.

# Média
print(dsa.mean(arr14))


# O desvio padrão é uma medida estatística de dispersão que indica o quanto os valores de um conjunto de dados
# se afastam da média. Ele é calculado como a raiz quadrada da variância, que é a média dos quadrados das
# diferenças entre cada valor e a média.
# 
# O desvio padrão é uma medida útil porque permite avaliar a variabilidade dos dados em torno da média. Se os
# valores estiverem próximos da média, o desvio padrão será baixo, indicando que os dados têm pouca
# variabilidade. Por outro lado, se os valores estiverem muito distantes da média, o desvio padrão será alto,
# indicando que os dados têm alta variabilidade.
# 
# O desvio padrão é amplamente utilizado em Análise e Ciência de Dados, para avaliar a consistência dos dados e
# comparar conjuntos de dados diferentes. É importante notar que o desvio padrão pode ser influenciado por
# valores extremos (outliers) e pode ser afetado por diferentes distribuições de dados.

# Desvio Padrão (Standard Deviation)
print(dsa.std(arr14))


# A variância é uma medida estatística que quantifica a dispersão dos valores em um conjunto de dados em
# relação à média. Ela é calculada como a média dos quadrados das diferenças entre cada valor e a média.
# 
# A fórmula para o cálculo da variância é:
# 
# var = 1/n * Σ(xi - x̄)^2
# 
# Onde:
# 
# - var é a variância
# - n é o número de observações
# - Σ é o somatório
# - xi é o i-ésimo valor no conjunto de dados
# - x̄ é a média dos valores
# 
# A variância é uma medida útil para avaliar a variabilidade dos dados em torno da média. Se a variância for
# baixa, isso indica que os valores estão próximos da média e têm pouca variabilidade. Por outro lado, se a
# variância for alta, isso indica que os valores estão distantes da média e têm alta variabilidade.

# Variância
print(dsa.var(arr14))


### Variância x Desvio Padrão ###

# Tanto a variância quanto o desvio padrão são medidas úteis de dispersão e podem ser usados em conjunto para
# descrever a distribuição de um conjunto de dados.
# 
# A variância é uma medida quadrática e pode ser útil para calcular outras estatísticas, como o desvio padrão.
# No entanto, como a variância é uma medida quadrática, seus valores são geralmente maiores do que os valores
# dos próprios dados, o que pode dificultar a interpretação. O desvio padrão é a raiz quadrada da variância e
# fornece uma medida de dispersão que tem a mesma unidade de medida que os próprios dados, facilitando a
# interpretação e a comparação com outros valores.
# 
# Em geral, o desvio padrão é mais comumente usado do que a variância, principalmente porque é mais fácil de
# interpretar. No entanto, a escolha entre o uso da variância ou do desvio padrão depende do contexto e do
# objetivo da análise. Em alguns casos, a variância pode ser uma medida mais apropriada, como quando se pretende
# calcular outras estatísticas, como a covariância ou o coeficiente de correlação. Em outros casos, o desvio
# padrão pode ser uma medida mais apropriada, como quando se pretende avaliar a consistência dos dados em
# relação à média e comparar diferentes conjuntos de dados.