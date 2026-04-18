#Faça um algoritmo em python capaz de realizar o cálculo de rentabilidade de uma poupança, esse algoritmo deve receber como entrada o valor inicial que o usuário está disposto a guardar. Como saída, o programa deve imprimir na tela mês a mês o montante por 12 mesesaplicado a uma taxa de 0,5 % ao mês de rentabilidade. A fórmula do montante (M) de uma aplicação financeira é dada por: M = P * (1 + i)^t

p = float(input("Digite o valor inicial: "))
i = 0.005  # taxa de 0,5% ao mês
t = 12     # período de 12 meses

for mes in range(1, t + 1):
    M = p * (1 + i) ** mes
    print(f"Mês {mes}: R$ {M:.2f}")