from cores import cores
import dados

cor = cores()

def opcoes():

    file = open('pessoas.txt','a')

    while True:
        dados.mostra_titulo('MENU PRINCIPAL')
        print(f'{cor["amarelo"]} 1) - {cor["azul"]} Ver pessoas cadastradas')
        print(f'{cor["amarelo"]} 2) - {cor["azul"]} Cadastrar nova pessoa')
        print(f'{cor["amarelo"]} 3) - {cor["azul"]} Sair do sistema{cor["limpa"]}')
        escolha = dados.valida_num(f'{cor["amarelo"]}Sua opcao: {cor["limpa"]}')

        if escolha in '1':
            dados.mostra_titulo("Pessoas cadastradas")
            lista = dados.le_pessoas()
            dados.le_lista(lista)


        elif escolha in '2':
            dados.cadastra_pessoa()

        elif escolha in '3':
            print('Encerrando...')
            break

        else:
            print(f'{cor["vermelho"]}Digite um numero valido.{cor["limpa"]}')





opcoes()

