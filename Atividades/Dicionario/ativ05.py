#Escreva uma função que receba um dicionário como entrada e retorna uma nova lista contendo apenas as chaves

dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

def extrair_chaves(dicionario):
    return list(dicionario.keys())

key_list = extrair_chaves(dicionario)
print("Chaves:", key_list)