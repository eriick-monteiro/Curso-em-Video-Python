# Mirim Infantil Junior Senior Master
from datetime import date
ano_de_nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - ano_de_nascimento

print(f'O atleta tem {idade} anos.')
print('Ele se classifica como ', end='')

# Classificando o atleta de acordo com a idade
if (idade <= 9):
    print('MIRIM')
elif (idade <= 14):
    print('INFANTIL')
elif (idade <= 19):
    print('JÚNIOR')
elif (idade <= 25):
    print('SÊNIOR')
elif (idade > 25):
    print('MASTER')
