import sys

def cores():

    cor = {'yellow':'\33[33m',
           'blue':'\33[34m',
           'clean':'\33[m',
           'red':'\033[31m'
    }

    return cor


def linha(tam =42):
    print('-'*tam)

def cabecalho(txt):
    tam =42
    linha()
    print(txt.center(tam))
    linha()


def leiaInt(txt):

    cor =cores()
    while True:
        try:
            n = int(input(txt))
        except (ValueError,TypeError):
            print(f'{cor["red"]}Digite um numero inteiro valido.{cor["clean"]}')
        except KeyboardInterrupt:
            print('Encerrando sistema.')
            sys.exit()
        else:
            return int(n)






def menu(lista):
    cor= cores()
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cor["yellow"]}{c} -  {cor["blue"]}{item}{cor["clean"]}')
        c+=1
    linha()
    resp = leiaInt(f'{cor["yellow"]}Sua opcao: {cor["clean"]}')
    return resp


