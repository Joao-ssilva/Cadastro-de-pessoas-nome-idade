def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError): # erro de valor ou erro de tipo.
            print('\033[31mPor favor, digite um número inteiro válido.\033[m ')
            continue
        except (KeyboardInterrupt): # erro de para o programa, parando manualmente ou ctrl+C
            print('Usúario preferiu não digitar esse número. ')
            return 0
        else:
            return n
        
def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc