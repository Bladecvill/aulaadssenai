#Escreva uma função que receba duas listas de mesmo comprimento, uma contendo chaves e outra contendo valores, e retorna um dicionário criado a partir dessas listas.

key_list = ["nome", "idade", "cidade"]
value_list = ["João", 30, "São Paulo"]

def criar_dicionario(keys, values):
    return dict(zip(keys, values))

dicionario = criar_dicionario(key_list, value_list)
print(dicionario)