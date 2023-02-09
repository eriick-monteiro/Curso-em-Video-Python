from random import randint
print('Suas Opções: ')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')

itens = ('pedra', 'papel', 'tesoura')
ia = randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))

# Se a escolha não for nenhuma acima, ele segue perguntando novamente
while jogador != 0 and jogador != 1 and jogador != 2:
    print('Escolha inesistente.')
    jogador = int(input('Qual é a sua jogada? '))

print('-=' * 11)
print(f'O computador escolheu {itens[ia]}')
print(f'Você escolheu {itens[jogador]}')
print('-=' * 11)

if (ia == 0): # Pedra
    if (jogador == 0): # Pedra
        print('Empatamos!')
    elif (jogador == 1): # Papel
        print('O Jogador EMBRULHOU a Pedra do Computador!')
    elif (jogador == 2): # Tesoura
        print('A Pedra do Computador ESMAGOU a Tesoura do Jogador!')
elif (ia == 1): # Papel
    if (jogador == 0): # Pedra
        print('O Papel do Computador EMBRULHOU a Pedrinha do Jogador!')
    elif (jogador == 1): # Papel
        print('Empatamos!')
    elif (jogador == 2): # Tesoura
        print('O Papel do Computador foi PICOTADO pela Tesoura do Jogador!')
elif (ia == 2): # Tesoura
    if (jogador == 0): # Pedra
        print('A Pedra do Jogador ESMIRALHOU a Tesoura do COmputador!')
    elif (jogador == 1): # Papel
        print('O Computador FATIOU diversas vezes o Papel do Jogador!')
    elif (jogador == 2): # Tesoura
        print('Empatamos!')