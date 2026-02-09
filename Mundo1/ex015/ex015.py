dias_alugados = int(input('Quantos dias alugado? '))
km_rodados = float(input('Quantos Km rodados? '))
valor_total = (dias_alugados * 60) + (km_rodados * 0.15)
print(f'O total a pagar é de R${valor_total}')
