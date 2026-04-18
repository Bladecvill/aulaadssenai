#Classificador de notas
#Crie uma função classificar_nota(nota) que receba uma nota e retorne "Excelente", "Aprovado", "Recuperação" ou "Reprovado" conforme a faixa. Chame a função para cada nota de uma lista usando for.

def classificar_nota(nota):
        if nota >= 9:
            return "Excelente"
        elif nota >= 7:
            return "Aprovado"
        elif nota >= 5:
            return "Recuperação"
        elif nota < 5:
            return "Reprovado"
        else:
            return "Nota inválida"

notas = [9, 7, 5, 3]
for nota in notas:
    resultado = classificar_nota(nota)
    print(f"Nota: {nota} - Classificação: {resultado}")