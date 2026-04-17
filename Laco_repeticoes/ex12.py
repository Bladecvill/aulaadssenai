r = input("Numeros par ou impar(P/I):").upper()
for i in range(1, 101):
    if r == "P" and i % 2 == 0:
        print("o valor ", i, "é par")
    elif r == "I" and i % 2 != 0:
        print("o valor", i, "é impar")
    elif r != "P" and r != "I":
        print("Entre com a letra correta")
        break