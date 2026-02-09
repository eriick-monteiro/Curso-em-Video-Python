valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento? '))
prestacao = valor / (anos / 12)
minimo = salario * 30 / 100

# Mostrando a prestação para o usuário
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos,', end='')
print(f' a prestação será de {prestacao:.2f}')

# Se a prestação for menor do que o mínimo, que é 30% do salário,
# ele concede o empréstimo, senão o empréstimo é recusado!
if (prestacao <= minimo):
    print('Empréstimo pode se CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
