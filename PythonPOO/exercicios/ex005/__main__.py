from classesex005 import Aluno, Professor, Funcionario
from rich import inspect


a1 = Aluno("João", 18, "Informática", "T01")
inspect(a1, methods=True)

p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
inspect(p1, methods=True)

f1 = Funcionario("Carlos", 63, "Designer", "Marketing")
inspect(f1, methods=True)

a1.fazer_matricula()
p1.dar_aula()
f1.bater_ponto()
