#0 - Peça para  o usuário entrar com dois valores (primeiro e último). Faça a contagem entre esses números. Caso o último for menor que  o primeiro faça a contagem decrescente. Caso o último número for maior que o primeiro faça a contagem crescente.

n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o segundo valor:"))

if n1 < n2:
    for i in range(n1, n2 + 1):
        print(i)
elif n1 > n2:

    for i in range(n1, n2-1, -1):
        print(i)
else:
    print("Digiteum valor válido")