from lib.interface import *
from lib.arquivo import *
from time import sleep
from os import system

system('cls')

nome_arquivo = 'cursoemvideo.txt'

if (archive_exists(nome_arquivo)):
    print('\033[32mArquivo encontrado com sucesso!\033[m')
else:
    print('\033[31mArquivo não encontrado!\033[m')
    create_archive(nome_arquivo)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Pessoas', 'Fechar Programa'])
    
    if (resposta == 1):
        # Opção de listar o conteúdo de um arquivo
        ler_arquivo(nome_arquivo)
    elif (resposta == 2):
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_inteiro('Idade: ')
        cadastrar_pessoa(nome_arquivo, nome, idade)
    elif (resposta == 3):
        cabecalho('\033[31mSaindo do Sistema... Até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)