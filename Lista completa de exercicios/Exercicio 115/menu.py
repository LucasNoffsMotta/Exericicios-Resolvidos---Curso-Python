from cores import cores
import dados
from time import sleep

cor = cores()

def opcoes():

    names_file = open('nomes.txt','a')



    while True:
        dados.mostra_titulo('MENU PRINCIPAL')
        sleep(0.5)
        print(f'{cor["amarelo"]} 1) - {cor["azul"]} Ver pessoas cadastradas')
        print(f'{cor["amarelo"]} 2) - {cor["azul"]} Cadastrar nova pessoa')
        print(f'{cor["amarelo"]} 3) - {cor["azul"]} Sair do sistema{cor["limpa"]}')
        escolha = dados.valida_num(f'{cor["amarelo"]}Sua opcao: {cor["limpa"]}')

        if escolha in '1':
            sleep(0.5)
            dados.mostra_titulo("PESSOAS CADASTRADAS")
            lista_nomes = dados.le_pessoas()
            dados.le_lista(lista_nomes)


        elif escolha in '2':
            sleep(0.5)
            dados.cadastra_pessoa()

        elif escolha in '3':
            print('Encerrando...')
            break

        else:
            print(f'{cor["vermelho"]}Digite um numero valido.{cor["limpa"]}')




