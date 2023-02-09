from datetime import date

# Coletando dados do usuário
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

# Se o usuário digitar ZERO, o ano vira o ano atual graças a biblioteca 'datetima'
if (ano == 0):
    date = date.today().year

# Anos divisíveis por 400 de resto 0 e divisíveis por 100 com resto diferente de 0 não são bissextos
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')