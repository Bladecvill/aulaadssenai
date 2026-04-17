# Faça um programa que peça ao usuário para digitar o número de vezes que ele quer jogar uma moeda.
#O programa deve simular o lançamento de uma moeda e imprimir o resultado de cada lançamento (cara ou coroa).
#No final, o programa deve imprimir o número total de caras e o número total de coroas.
#Use a biblioteca abaixo para números aleatórios:

import random

n = int(input("Digite o numero de vezes que quer jogar a moeda: "))
caras = 0
coroas = 0

for i in range(n):
    resultado = random.randint(0, 1)
    if resultado == 0:
        print("Cara")
        caras += 1
    else:
        print("Coroa")
        coroas += 1

print(f"Total de caras: {caras}")
print(f"Total de coroas: {coroas}")
