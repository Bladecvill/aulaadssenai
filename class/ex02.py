class Pessoa:
    def __init__(self, nome = None, idade = None):
        if nome is None:
            nome = input("Digite o nome: ")
        
        if idade is None:
            idade = int(input("Digite a idade: "))
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("=" * 10)
        print("Olá", self.nome)
        print("Você tem:", self.idade)

pessoa1 = Pessoa()
pessoa1.apresentar()

aluna = Pessoa("Ana", 21)
aluna.apresentar()