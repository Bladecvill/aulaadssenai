#Escreva um código que verifique se uma pessoa é alfabetizada (sabe ler e escrever) e tem mais de 25 anos de idade.

alfabetizada = input("Você é alfabetizado? (sim/não): ") 
idade = int(input("Qual sua idade? "))

if alfabetizada.lower() == "sim" and idade > 25:
    print("A pessoa é alfabetizada e tem mais de 25 anos.")
else:
    print("A pessoa não atende aos requisitos.")
