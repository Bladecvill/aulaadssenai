#Tabuada personalizada
#Crie uma função tabuada(numero) que use while para gerar e exibir a tabuada de um número de 1 a 10. Depois, use um for para chamar a função com cada número de uma lista como [2, 5, 7].

def tabuada(numero):
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1

numeros = [2, 5, 7]
for n in numeros:
    print(f"Tabuada do {n}:")
    tabuada(n)
    print("=" * 20) 