#Escreva uma função que receba um dicionário como entrada e retorna uma nova lista com as chaves ordenadas em ordem alfabética.

dicionario = {"z": 3, "t": 1, "a": 2}

def ordenar_chaves(dicionario):
    return sorted(dicionario.keys())

ordered_keys = ordenar_chaves(dicionario)
print("Chaves ordenadas:", ordered_keys)