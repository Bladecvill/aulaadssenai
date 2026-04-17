#Verifique se uma pessoa é maior ou igual a 18 anos ou se ela tem autorização dos pais

age = int(input("Digite a sua idade: "))
auth = input("Você tem autorização dos pais? (S/N)")

if age >= 18 or auth.upper() == "S":
    print("Você é maior de idade ou tem autorização dos pais.")
else:
    print("Você não é maior de idade ou não tem autorização dos pais.")