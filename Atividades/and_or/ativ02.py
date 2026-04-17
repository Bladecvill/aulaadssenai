#Escreva um programa que peça ao usuário inserir duas notas (entre 0 e 100) e determine se o aluno passou ou não. Um aluno passa se a soma das notas for maior ou igual 
#a 60 e nenhuma nota é menor que 40.

nt1 = int(input("Digite a primeira nota: "))
nt2 = int(input("Digite a segunda nota: "))

if nt1 >= 40 and nt2 >= 40 and nt1 + nt2 >= 60:
    print("O aluno passou!")
else:
    print("Aluno reprovado")