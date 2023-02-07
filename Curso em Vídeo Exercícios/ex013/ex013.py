salario = float(input('Qual é o salário do funcionário? R$'))
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${salario + (salario * 15 / 100):.2f}')