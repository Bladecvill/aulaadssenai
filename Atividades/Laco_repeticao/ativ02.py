# Faça um programa que peça ao usuário para adivinhar um número entre 1 e 100.
#Enquanto o número digitado não for igual a um número secreto definido pelo programa,
#o programa deve pedir ao usuário que tente novamente. Quando o usuário acertar o número,
#o programa deve imprimir "Parabéns, você acertou!".
#Use a biblioteca abaixo para números aleatórios:

import random
ns = random.randint(1,100)
n = int(input("Adivinhe o numero:"))

while n != ns:
    if n > ns:
            print("dica: é menos")
    else:
            print("dica: é mais")

    n = int(input("Tente novamente:"))


print("Ta de hack")