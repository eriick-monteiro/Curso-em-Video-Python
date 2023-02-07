largura = float(input('Largura da perede: '))
altura = float(input('Altura da perede: '))
area = largura*altura
tinta_necessaria = area / 2
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta_necessaria}l de tinta.')