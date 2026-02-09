from math import trunc
valor = float(input('Digite um valor: '))
print(f'O valor digitado foi {valor} e a sua porção inteira é {trunc(valor)}')

# Outro jeito seria:
# print(f'O valor digitado foi {valor} e a sua porção inteira é {valor:.0f}')
