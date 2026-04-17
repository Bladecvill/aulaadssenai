# Leia dois números
n1 = float(input("Entre com o primeiro número: "))
n2 = float(input("Entre com o segundo número: "))
n3 = float(input("Entre com o terceiro número: "))

# Escolha o maior

if n1 > n2 and n1 > n3:
        maior_numero = n1
        
elif n2 > n1 and n2 > n3:
    maior_numero = n2

elif n3 > n1 and n3 > n2:
    maior_numero = n3
else:
    print("Há números iguais")


# imprima o resultado
print("O maior número é:", maior_numero)