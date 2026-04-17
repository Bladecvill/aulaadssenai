print("Lista par 'Alugel de automoveis'")
age = int(input("Digite sua idade:"))
money = int(input("Digite quantos reais você tem:"))
cnh = int(input("Possue cnh? (s/n)"))
if (age <= 18 and money >= 50) or cnh == "s":
    print("Você pode alugar um carro")
else:
    print("Soliciação negada")