# Leia dois números
n1 = float(input("Entre com o primeiro número: "))
n2 = float(input("Entre com o segundo número: "))
n3 = float(input("Entre com o terceiro número: "))

# Escolha o maior

if n1 > n2:
    if n1 > n3:
        maior_numero = n1
    else:
        if n3 > n2:
            maior_numero = n3
        else:
            maior_numero = n2

else:
    if n2 > n3:
        maior_numero = n2
    else:
        maior_numero = n3

# imprima o resultado
print("O maior número é:", maior_numero)