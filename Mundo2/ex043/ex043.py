peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é {imc:.1f}')

# Mostrando o resultado de acordo com o IMC
if (imc < 18.5):
    print('Está abaixo do peso.')
elif (imc >= 18.5 and imc <= 24.99):
    print('Está com peso normal.')
elif (imc >= 25.0 and imc <= 29.99):
    print('Está acima do peso.')
elif (imc >= 30.0):
    print('Está muito acima do peso.')
