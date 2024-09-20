# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science == CAPÍTULO 4

### PARTE 5 == Dicionários ###

### Trabalhando com Dicionários ###

# Isso é uma dicta:
estudantes_list = ["Pedro", 24, "Ana", 22, "Ronaldo", 26, "Janaina", 25]
print(estudantes_list)
print(type(estudantes_list))

# Isso é um dicionário:
estudantes_dict = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}
print(estudantes_dict)
print(type(estudantes_dict))

print(estudantes_dict["Pedro"])

# adicionar chave no dicionário ou editar valor da chave
estudantes_dict["Marcelo"] = 23
print(estudantes_dict)

estudantes_dict.clear()
print(estudantes_dict)

del estudantes_dict
# print(estudantes_dict)


estudantes = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}

print(estudantes)
print(len(estudantes))

estudantes_v = estudantes.values()
print(estudantes_v)

estudantes_i = estudantes.items()
print(estudantes_i)


estudantes2 = {"Camila": 27, "Adriana": 28, "Roberta": 26}

print(estudantes2)

estudantes.update(estudantes2)
print(estudantes)


dict1 = {}

print(dict1)

dict1["chave_um"] = 2
print(dict1)

dict1[10] = 5
print(dict1)

dict1[9.13] = "Python"
print(dict1)

dict1["teste"] = 5
print(dict1)


# Dicionário de listas

dict2 = {"chave1": 1230, "chave2": [22, 453, 73.4], "chave3": ["picanha", "fraldinha", "alcatra"]}

print(dict2)

print(dict2["chave2"])

# Acessando um item da lista, dentro do dicionário
var1 = dict2["chave3"][0].upper()
print(var1)

# Operações com itens da lista, dentro do dicionário
var2 = dict2["chave2"][0] - 2
print(var2)

# Duas operações no mesmo comando, para atulizar um item dentro da lista
# obs "-=" -> notação que simplifica!
dict2["chave2"][0] -= 2
print(dict2)

# Criando dicionários aninhados (é possível, mas não recomendado)

dict_aninhado = {"key1": {"key2_aninhada": {"key3_aninhada": "Dict aninhado em Python"}}}
print(dict_aninhado)

# quero buscar esse elemento "Dict aninhado em Python"
print(dict_aninhado["key1"]["key2_aninhada"]["key3_aninhada"])

print("-"*50)