# Função para encontrar números repetidos e suas posições
def encontrar_repetidos(vet):
    repetidos = {}
    for i, num in enumerate(vet):
        if num in repetidos:
            repetidos[num].append(i)
        else:
            repetidos[num] = [i]
    
    # Exibir os números repetidos e suas posições
    tem_repetidos = False
    for num, posicoes in repetidos.items():
        if len(posicoes) > 1:
            tem_repetidos = True
            print(f"Número {num} repetido nas posições: {posicoes}")
    
    if not tem_repetidos:
        print("Não há números repetidos no vetor.")

# Leitura de 10 números e armazenamento no vetor
VET = []
for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    VET.append(numero)

# Chamada da função para encontrar e exibir os repetidos
encontrar_repetidos(VET)
