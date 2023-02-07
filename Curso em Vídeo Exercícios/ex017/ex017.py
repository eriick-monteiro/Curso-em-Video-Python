cateto_oposto = float(input('Comprimento do Cateto Oposto: '))
cateto_adjacente = float(input('Comprimento do Cateto Adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print(f'A Hipotenusa vai medir {hipotenusa:.2f}')