
### While e For Juntos ###
    # Vamos encontrar números primos em uma coleção de números usando loop While e For juntos.

# Aqui está o pseudocódigo:
    # Inicialize uma lista vazia para armazenar os números primos
    # Para cada número N entre 2 e 30:
    #   Inicialize uma variável eh_primo como verdadeira
    #   Para cada número i entre 2 e N/2:
    #     Se N é divisível por i, então:
    #       Altere a variável eh_primo para falso
    #       Pare de verificar os outros números
    #   Se a variável eh_primo ainda é verdadeira, adicione N à lista de números primos
    # Imprima a lista de números primos


# Medindo o tempo de execução no jupyer == %%time, %timeit
# Medindo o tempo de execução
import timeit
tempo_execucao = timeit.timeit('sum(range(1000))', number=10000)
print(f"Tempo de execução: {tempo_execucao} segundos")


# Encontrando números primos entre 2 e 30 usando loop for e while

# Variável para armazenar números primos
primos = []

# Loop for para percorrer números de 2 a 30
for num in range(2, 31):
    
    # Variável de controle
    eh_primo = True
    
    # Loop while para verificar se o número é primo
    i = 2
    while i <= num // 2:
        if num % i == 0:
            eh_primo = False
            break
        i += 1
    
    # Adicionando o número primo na lista
    if eh_primo:
        primos.append(num)

# Imprimindo a lista de números primos
print(primos)

print("-"*50)