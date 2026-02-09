from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento

if (idade == 18):
    print('Você tem que se alistar IMEDIATAMENTE.')
elif (idade < 18):
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano_de_alistamento = ano_atual + saldo
    print(f'Seu alistamento será em {ano_de_alistamento}.')
elif (idade > 18):
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {saldo} anos.')
    ano_de_alistamento = ano_atual - saldo
    print(f'Seu alistamento foi em {ano_de_alistamento}.')
