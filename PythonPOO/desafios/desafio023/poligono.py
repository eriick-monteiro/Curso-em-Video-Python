from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, lados):
        self.qtd_lados = lados


    @abstractmethod
    def perimetro(self):
        pass


    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        self.lado = lado
        self.qtd_lados = 4


    def perimetro(self):
        return self.qtd_lados * self.lado


    def area(self):
        return self.lado**2


class Circulo(Poligono):
    def __init__(self, raio):
        self.raio = raio


    def perimetro(self):
        return ((2 * 3.14) * self.raio)


    def area(self):
        return (3.14 * self.raio**2)

