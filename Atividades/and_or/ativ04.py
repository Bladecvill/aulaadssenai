#Escreva um código que verifique se um número é par ou divisível por 3.

n1 = int(input("Digite um número: "))

if n1 % 2 == 0:
    print("O número é par.")

elif n1 % 3 == 0:
    print("O número é divisivel por 3")

else:
    print("O númer não é nada")