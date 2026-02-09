distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}Km.')

# Definindo o valor da passagem
if (distancia <= 200):
    preco = distancia * .5
else:
    preco = distancia * .45

print(f'E o preço da sua passagem será de R${preco:.2f}')
