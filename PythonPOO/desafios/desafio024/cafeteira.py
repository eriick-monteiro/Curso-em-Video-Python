from abc import ABC, abstractmethod


class BebidaQuente(ABC):

    # Métodos
    def preparar(self):
        print("--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida Pronta ---")


    def ferver_agua(self):
        print("1. Fervendo a água a 100 graus Celsius.")


    @abstractmethod
    def misturar(self):
        pass


    @abstractmethod
    def servir(self):
        pass


class Leite(BebidaQuente):

    # Métodos
    def misturar(self):
        print("2. Vapor pressurizado pelo bico do leite.")


    def servir(self):
        print("3. Sevindo na caneca grande, já com café.")


class Cafe(BebidaQuente):

    # Métodos
    def misturar(self):
        print("2. Passando água pressurizada pelo pó de café moído.")


    def servir(self):
        print("3. Sevindo em xícara pequena.")


class Cha(BebidaQuente):

    # Métodos
    def misturar(self):
        print("2. Mergulhando sache de ervas na agua.")


    def servir(self):
        print("3. Sevindo em uma caneca de porcelana com maracujá.")
