class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor > 0:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque deve ser positivo.")

    def mostrar_saldo(self):
        print("Saldo atual:", self.__saldo)
    
    def mostrar_titular(self):
        print("Titular da conta:", self.__titular)

conta = ContaBancaria("Ana")
conta.depositar(5000)
conta.sacar(1500)
conta.mostrar_saldo()
conta.mostrar_titular()