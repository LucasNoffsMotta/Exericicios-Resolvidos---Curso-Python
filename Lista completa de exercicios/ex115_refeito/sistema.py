from libary.interface import *
from libary.arquivo import *
from time import sleep

cor= cores()

while True:
    resposta = menu(['Cadastro de pessoas','Ver pessoas cadastradas','Sair'])

    if resposta == 1:
        status = check_file()
        if not status:
            make_file('Dados')
            nome = input('Nome: ')
            idade = leiaInt('Idade: ')
            cadastrar('Dados',nome,idade)

    elif resposta == 2:
        cabecalho('Pessoas cadastradas')
        read_file('Dados')



    elif resposta == 3:
        cabecalho('Saindo')
        break

    else:
        print(f'{cor["red"]}Digite um numero valido!{cor["clean"]}')
    sleep(2)