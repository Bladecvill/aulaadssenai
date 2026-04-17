#Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

n = int(input("Digite um número entre 1 e 10: "))
i = 0
if n <= 10 and n >= 1:
    while i <= 10:
        print(n, "x", i, "=", n * i)
        i += 1
else:
    print("Digite um valor de 1 a 10")