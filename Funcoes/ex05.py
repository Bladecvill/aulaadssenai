def calcular_media(md):
    nmd = sum(md)
    media = nmd / len(md)

    return media

def verificacao(media):
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"
    
md = [7.5, 8.0, 6.5, 9.0]
media = calcular_media(md)
print("A média é: ", media)

situacao = verificacao(media)
print("Você foi", situacao)