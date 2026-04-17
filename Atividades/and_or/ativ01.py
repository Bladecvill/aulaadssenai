#Escreva um programa que peça ao usuário inserir três números e, em seguida, determine se um dos três números é maior que a soma dos outros dois.

n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
n3 = int(input("Digite mais um número:"))

if n1 > n2 + n3:
    print("maior que n2 + n3", n1)

elif n2 > n1 + n3:
    print("maior que n1 + n3", n2)

elif n3 > n1 + n2:
    print("maior que n1 + n2", n3)

else:
    print("numeros iguais")