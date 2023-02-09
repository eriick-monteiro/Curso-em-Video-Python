from os import system
from time import sleep

def fakeProgress():
    for i in range(100):
        i+=1
        print(f"\033[0;34;40mConcluindo [{i}%]\033[0;37;40m")
        system('cls')

#Limpando o Terminal
system('cls')

#Coletando o numero do usuário
num = int(input('Digite aqui o número que deseja converter: '))

#Limpando o Terminal novamente (x2)
system('cls')

#Colocando o programa em uma função para poder ser "loopado"
def conversor():
    #Mostrando as opções para o usuário
    option = int(input(f'''\033[0;35;40m
    [1] - Binário
    [2] - Octal
    [3] - Hexadecimal
    \033[0;37;40mAgora escolha uma das bases para converter \033[0;34;40m{num}: \033[0;37;40m'''))

    #Limpando o Terminal novamente (x3)
    system('cls')

    #Colocando um falso progresso para dar estilo ao programa
    fakeProgress()
    print('\033[0;34;40mConcluído [100%]\033[0;37;40m')
    sleep(1)

    #Limpando o Terminal novamente (x4)
    system('cls')

    #Dependendo da opção, o programa mostra a operação selecionada
    if (option == 1):
        print(f'{num} convertido em Binário é: \033[0;32;40m{bin(num)[2:]}\033[0;37;40m')
    elif (option == 2):
        print(f'{num} convertido em Octal é: \033[0;32;40m{oct(num)[2:]}\033[0;37;40m')
    elif (option == 3):
        print(f'{num} convertido em Hexadecimal é: \033[0;32;40m{hex(num)[2:]}\033[0;37;40m')
    else:
        print(f'\033[0;31;40m{option} não é uma opção válida! Tente novamente.\033[0;37;40m\n')
        conversor()

#Iniciando o programa pela primeira vez
conversor()