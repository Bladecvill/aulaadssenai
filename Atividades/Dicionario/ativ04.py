#Escreva uma função que receba um dicionário como entrada e retorna duas listas. Uma com chave e outra com valor.

dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

def separar_chaves_valores(dicionario):
    chaves = list(dicionario.keys())
    valores = list(dicionario.values())
    return chaves, valores

key_list = separar_chaves_valores(dicionario)[0]
value_list = separar_chaves_valores(dicionario)[1]
print("Chaves:", key_list)
print("Valores:", value_list)