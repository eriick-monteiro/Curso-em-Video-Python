print('==========CoderBoy Store==========')
valor = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista em dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção que deseja? '))

if (opcao == 1):
    total = valor - (valor * 10 / 100)  # Dando desconto de 10% por ser à vista
elif (opcao == 2):
    total = valor - (valor * 5 / 100)  # Dando desconto de 5% por ser à vista
elif (opcao == 3):
    total = valor
    parcela = total / 2
    print(f'A compra será parcelada em 2x de R${parcela:.2f}')
elif (opcao == 4):
    total = valor + (valor * 20 / 100)  # Dividir em mais vzs tem juros de 20%
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print(f'A compra será parcelada em {total_parcelas}x de R${parcela:.2f}')
else:
    total = 0
    print('OPÇÃO DE PAGAMENTO INVÁLIDA! Tente novamente.')

# Printando o valor anterior e o novo
print(f'A compra de R${valor:.2f} vai custar R${total:.2f} no final.')
print()
print('=-='*15)
print('   Obrigado por Comprar na CoderBoy Store')
print('=-='*15)
