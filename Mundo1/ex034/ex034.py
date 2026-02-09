salario = float(input('Qual é o salário do funcionário? R$'))

# Se o salário for menor ou igual a R$1.250
# o funcionário recebe 15% de aumento,
# se for maior, recebe 10% de aumento.
if (salario <= 1250):
    print(f'Quem ganhava R${salario} passa a ganhar R${salario + (salario * 15 / 100):.2f}')
else:
    print(f'Quem ganhava R${salario} passa a ganhar R${salario + (salario * 10 / 100):.2f}')
