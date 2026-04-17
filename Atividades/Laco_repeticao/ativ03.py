
soma = 0
while True:
    num = int(input("Digite um número inteiro (ou um número negativo para parar): "))
    if num < 0:
        break
    soma += num
print(f"A soma dos números é: {soma}")
