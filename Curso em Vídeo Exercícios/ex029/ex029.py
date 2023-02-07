velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if (velocidade > 80):
    print(f'\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    print(f'\033[31mVocê deve pagar uma multa de R${multa:.2f}')
print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')