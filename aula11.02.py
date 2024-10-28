import random

# Criação da matriz A com valores randômicos entre 1 e 100
A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

# a. Soma de todos os valores da matriz A
soma_total = sum(sum(linha) for linha in A)
print("Soma de todos os valores da matriz A:", soma_total)

# b. Criação da matriz B com cada elemento de A multiplicado por 3
B = [[elemento * 3 for elemento in linha] for linha in A]

# Impressão das matrizes A e B para visualização
print("\nMatriz A:")
for linha in A:
    print(linha)

print("\nMatriz B (elementos de A * 3):")
for linha in B:
    print(linha)
