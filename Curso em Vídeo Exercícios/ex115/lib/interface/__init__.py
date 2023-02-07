def leia_inteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return numero

def linha(tam=42):
    return '-' * tam

def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1

    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1

    print(linha())
    opcao = leia_inteiro('\033[32mSua Opção: \033[m')
    return opcao