#Criar um programa que verifica se uma pessoa tem desconto em um produto, baseado na idade e sua categoria (estudante, aposentado, etc.) e no dia da semana. (Use quantas categorias desejar)

idade = int(input("Qual a sua idade? "))
categoria = input("Qual a sua categoria (estudante, aposentado, comum)? ").lower()
dia_semana = input("Qual o dia da semana? ").lower()

desconto = 0

if (categoria == "estudante" or categoria == "aposentado") and (dia_semana == "segunda" or dia_semana == "terça" or dia_semana == "quarta" or dia_semana == "quinta" or dia_semana == "sexta"):
    desconto = 10
elif idade > 60:
    desconto = 15

if desconto > 0:
    print(f"Você tem {desconto}% de desconto.")
else:
    print("Você não tem direito a desconto.")
