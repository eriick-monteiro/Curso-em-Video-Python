from funcionario import *


def main():
    f1 = FuncionarioHorista(nome="Paulo", valor_hora=12, horas_trabalhadas=200)
    f1.calcular_salario()
    f1.analisar_salario()


    f2 = FuncionarioMensalista(nome="Amanda", salario_bruto=9500)
    f2.calcular_salario()
    f2.analisar_salario()



if __name__ == "__main__":
    main()
