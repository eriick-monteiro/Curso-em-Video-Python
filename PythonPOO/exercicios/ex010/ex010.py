class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # Métodos acessores
    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, nota):
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("Nota inválida")

    @nota.deleter
    def nota(self):
        pass

    def __str__(self):
        return  f"Estado atual da avaliação: {self.__dict__}"
