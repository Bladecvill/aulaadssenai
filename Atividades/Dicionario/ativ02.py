#Escreva uma função que receba Nome e Idade. Retorne valores que contêm a chave "idade" e cujo valor é maior que 18.

dicionario = {"nome": "João", "idade": 20, "nome2": "Maria", "idade2": 17}

def verificar_idade(dicionario):
    if dicionario["idade"] >= 18:
        return {"nome": dicionario["nome"], "idade": dicionario["idade"], "mensagem": "Maior de idade"}
    else:
        return {"nome": dicionario["nome"], "idade": dicionario["idade"], "mensagem": "Menor de idade"}
    

print(verificar_idade(dicionario))
