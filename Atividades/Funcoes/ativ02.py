#Contador de positivos e negativos
#Crie uma função analisar_numeros(lista) que percorra uma lista com for e retorne quantos números são positivos, negativos e zeros. Teste com uma lista de pelo menos 6 números.

def analisar_numeros(lista):
    positivos = 0
    negativos = 0
    zeros = 0
    
    for numero in lista:
        if numero > 0:
            positivos += 1

        elif numero < 0:
            negativos += 1

        elif numero == 0:
            zeros += 1
            
    return {"positivos": positivos, "negativos": negativos, "zeros": zeros}

numeros = [1, -2, 0, 3, -4, 5]
resultado = analisar_numeros(numeros)
print("Análise dos números:", resultado)