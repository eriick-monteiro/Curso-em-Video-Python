# Declaração da classe
class Gafanhoto:
    """
Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use:
variavel = Gafanhoto(nome, idade)
    """

    def __init__(self, nome="", idade=0):  # Método construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"


# Declaração dos objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)

print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)

print(Gafanhoto.__doc__)
