#Escreva uma função que receba itens (números) em um dicionário como entrada e retorne a chave com o maior valor.

def maior_valor(dicionario):
    if not dicionario:
        return None
    
    return max(dicionario, key=dicionario.get)

numeros = {'a': 5, 'b': 2, 'c': 8, 'd': 1}

maior_valor(numeros)