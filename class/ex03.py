class Calculadora:
    def __init__(self, num1 = None, num2 = None):
        if num1 is None:
            num1 = float(input("Digite o primeiro número: "))
        if num2 is None:
            num2 = float(input("Digite o segundo número: "))

        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2

    def subtracao(self):
        return self.num1 - self.num2

    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Erro: Divisão por zero"
    
    def selecionar_operacao(self):
        print("Selecione a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        escolha = input("Digite o número da operação desejada: ")
        return escolha
    
        
calc = Calculadora()
print("Soma:", calc.soma())
print("Subtração:", calc.subtracao())
print("Multiplicação:", calc.multiplicacao())
print("Divisão:", calc.divisao())