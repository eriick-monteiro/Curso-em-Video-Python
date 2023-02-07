from lib.interface import *

def archive_exists(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt') # abrir em modo Read Text
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True

def create_archive(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'wt+') # Write Text - o '+' significa que se o arquivo não existe, ele o cria
        arquivo.close()
    except:
        print('\033[31mHOuve um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[34mArquivo {nome_arquivo} criado com sucesso!\033[m')

def ler_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt')
    except:
        print('\033[31mHOuve um erro ao abrir arquivo!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close()

def cadastrar_pessoa(nome_arquivo, nome='Desconhecido', idade='???'):
    try:
        arquivo = open(nome_arquivo, 'at') # 'a' de append e 't' de text, acescentar dados
    except:
        print('\033[31mHOuve um erro ao abrir arquivo!\033[m')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHOuve um erro na hora de escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado!')
            arquivo.close()