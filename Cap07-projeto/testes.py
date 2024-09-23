import random

def escolher_palavra():
    # Definindo as categorias e suas palavras
    categorias = {
        "animais": ["leão", "tigre", "elefante", "cachorro", "gato", "golfinho"],
        "frutas": ["morango", "banana", "laranja", "uva", "abacaxi", "kiwi"]
    }
    
    # Escolhendo aleatoriamente entre as categorias
    categoria_escolhida = random.choice(list(categorias.keys()))
    
    # Escolhendo uma palavra aleatória dentro da categoria escolhida
    palavra_escolhida = random.choice(categorias[categoria_escolhida])
    
    dict_chosen = {categoria_escolhida: palavra_escolhida}
    
    print(dict_chosen)
    
    print(f"Categoria escolhida: {categoria_escolhida.capitalize()}")
    print(f"Palavra escolhida: {palavra_escolhida.capitalize()}")

# Exemplo de uso
escolher_palavra()
