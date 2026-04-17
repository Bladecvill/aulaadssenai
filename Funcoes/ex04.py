def funcao_detecta(n):
    if (n % 2 == 0):
        return "é par"
    else:
        return "é impar"
    
print(funcao_detecta(int(input("Digite um numero: "))))