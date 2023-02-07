from random import randint
from time import sleep
print('\033[33m-=' * 35)
print('\033[34mVou pensar em um número aleatório entre 0 a 5. Tente adivinhar...')
print('\033[33m-=\033[m' * 35)
numero = randint(0, 10)
tentativa = int(input('Em que número eu pensei? '))

print('\033[35mPROCESSANDO...')
sleep(2)

if (tentativa == numero):
    print('\033[33mPARABÉNS!Você conseguiu me vencer!\033[m')
else:
    print(f'\033[31mGANHEI! Eu pensei no número {numero} e não no {tentativa}\033[m')