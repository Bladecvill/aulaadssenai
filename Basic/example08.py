#Calculadora de média
nt1 = float(input("Digite a nota 1: "))
nt2 = float(input("Digite a nota 2: "))
nt3 = float(input("Digite a nota 3: "))
nt4 = float(input("Digite a nota 4: "))

#Formula da média
media = (nt1 + nt2 + nt3 + nt4) / 4

print("A média é: ", media)


if  media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")