
# Medindo o tempo de execução no jupyer == %%time, %timeit
# Medindo o tempo de execução
import timeit
tempo_execucao = timeit.timeit('sum(range(1000))', number=10000)
print(f"Tempo de execução: {tempo_execucao} segundos")

# Encontrando números primos entre 2 e 30 usando loop for e while (outro exemplo)

# Loop for para percorrer números de 2 a 30
for i in range(2,31):
    
    # Variável de controle
    j = 2
    
    # Contador
    valor = 0
    
    # Loop while para verificar se o número é primo
    while j < i:
        if i % j == 0:
            valor = 1
            j = j + 1
        else:
            j = j + 1
    
    if valor == 0:
        print(str(i) + " é um número primo")
        valor = 0
    else:
        valor = 0
        
print("-"*50)