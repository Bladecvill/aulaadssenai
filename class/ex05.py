class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque deve ser positivo.")

    def consultar_saldo(self):
        status = "positivo" if self.__saldo >= 0 else "negativo"
        print(f"Saldo atual: R${self.__saldo:.2f} [{status}]")

    def get_titular(self):
        return self.__titular

class Banco:
    def __init__(self):
        self.correntista = []

    def criar_conta(self):
        nome = input("Digite o nome do titular da conta: ")
        conta = ContaBancaria(nome)
        self.correntista.append(conta)
        print(f"Conta criada para {nome}.")

    def buscar_conta(self, nome):
        for conta in self.correntista:
            if conta.get_titular() == nome:
                return conta
        
        print("Conta não encontrada.")
        return None
    
    def depositar_fundos(self):
        nome = input("Digite o nome do titular da conta: ")
        conta = self.buscar_conta(nome)
        if conta:
            try:
                valor = float(input("Digite o valor a ser depositado: "))
                conta.depositar(valor)
            except ValueError:
                print("Valor inválido. Por favor, insira um número.")
        else:
            print("Correntista não encontrado.")    
    
    def sacar_fundos(self):
        nome = input("Digite o nome do titular da conta: ")
        conta = self.buscar_conta(nome)
        if conta:
            try:
                valor = float(input("Digite o valor a ser sacado: "))
                conta.sacar(valor)
            except ValueError:
                print("Valor inválido. Por favor, insira um número.")
        else:
            print("Correntista não encontrado.")
    
    def consultar_saldo_correntista(self):
        nome = input("Digite o nome do titular da conta: ")
        conta = self.buscar_conta(nome)
        if conta:
            conta.consultar_saldo()
        else:
            print("Correntista não encontrado.")
    
    def listar_correntistas(self):
        for conta in self.correntista:
            print(f"Titular: {conta.get_titular()} || Saldo: R${conta._ContaBancaria__saldo:.2f}")

def main():
    banco = Banco()
    while True:
        print("\n--------Menu--------")
        print("1. Criar conta")
        print("2. Depositar fundos")
        print("3. Sacar fundos")
        print("4. Consultar saldo")
        print("5. Listar correntistas")
        print("6. Sair")
        
        print("=" * 20)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            banco.criar_conta()
        elif opcao == '2':
            banco.depositar_fundos()
        elif opcao == '3':
            banco.sacar_fundos()
        elif opcao == '4':
            banco.consultar_saldo_correntista()
        elif opcao == '5':
            banco.listar_correntistas()
        elif opcao == '6':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

main()