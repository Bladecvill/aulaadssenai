class Forma:
    def area(self):
        pass
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

class Trapézio(Forma):
    def __init__(self, base_maior, base_menor, altura):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura

    def area(self):
        return ((self.base_maior + self.base_menor) / 2) * self.altura

formas = [Retangulo(10, 5), Triangulo(10, 5),]
for forma in formas:
    print(f"A área da {forma.__class__.__name__} é: {forma.area()}")