n = int(input("Digite um numero:"))
i = 0
for i in range(2, n):
    if n % i == 0:
        print("O numero", n , "Não é primo")
        break
else:
        print("O numero", n , "É primo")