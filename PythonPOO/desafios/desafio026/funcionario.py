from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print


class Funcionario(ABC):
    def __init__(self, nome, salario_bruto, salario=0, salario_minimo = 1612, inss = 7.5):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario = salario
        self.salario_minimo = salario_minimo
        self.inss = inss


    @abstractmethod
    def calcular_salario(self):
        pass


    def analisar_salario(self):
        mensagem = f"O salário de [blue]{self.nome}[/] ([purple]{type(self).__name__}[/]) é de [green]R${self.calcular_salario():.2f}[/] e corresponde a [yellow]{(self.calcular_salario() / self.salario_minimo):.1f} salários mínimos[/]"
        painel = Panel(mensagem, title="Análise de Salário", width=50)

        print(painel)


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):

        super().__init__(nome, salario_bruto=0, salario=0)

        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas


    def calcular_salario(self):
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas
        self.salario = self.salario_bruto - (self.salario_bruto * (self.inss / 100))

        return self.salario


class FuncionarioMensalista(Funcionario):
    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * (self.inss / 100))

        return self.salario