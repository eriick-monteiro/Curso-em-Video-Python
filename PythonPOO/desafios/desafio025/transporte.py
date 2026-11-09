from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia, frete=0):
        self.distancia = distancia
        self.frete = frete


    @abstractmethod
    def calcular_frete():
        pass


class Caminhao(Transporte):

    def calcular_frete(self):
        self.fator = 1.20

        if self.distancia < 50:
            return "Raio mínimo de 50Km"
        else:
            return f"R${self.distancia*self.fator:.2f}"


class Moto(Transporte):

    def calcular_frete(self):
        self.fator = 0.50

        return f"R${self.distancia*self.fator:.2f}"


class Drone(Transporte):

    def calcular_frete(self):
        self.fator = 9.50

        if self.distancia > 10:
            return "Raio máximo de 10Km"
        else:
            return f"R${self.distancia*self.fator:.2f}"
