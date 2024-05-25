import cores

cor = cores.cores()


def mostra_titulo(txt):
    tam = 28 + 15

    print('-'*tam)
    print(txt.center(tam))
    print('-'*tam)

def valida_num(txt):

    while True:
        print('-'*(28 + 15))
        opcao = str(input(txt))

        try:
            int(opcao)
        except ValueError:
            print(f'{cor["vermelho"]}ERRO. Entrada invalida.{cor["limpa"]}')
        except KeyboardInterrupt:
            print(f'{cor["verde"]}Encerrando...')
        else:
            return opcao



def cadastra_pessoa():

    pessoas_cadastradas = list()

    nome = (str(input('Nome: '))).strip()
    if nome.strip() == '':
        nome = 'Vazio'
    idade = valida_num("Idade: ")

    pessoas_cadastradas.append(nome)
    pessoas_cadastradas.append(idade)


    with open('nomes.txt','a') as file:
        for pessoa in pessoas_cadastradas:
            file.write(pessoa + '\n')


    file.close()



def le_pessoas():

    lista = []

    with open('nomes.txt','r') as documento:

        linha = documento.readlines()
        if linha != '':
            lista.append(linha)


    documento.close()

    return lista


def le_lista(lista_nomes):

    lista_final_nomes = list()
    lista_final = list()


    for lista1 in lista_nomes:
        lista_final_nomes = lista1


    for num,nome in enumerate(lista_final_nomes):
        nome_ajustado = nome.strip('\n')
        lista_final.append(nome_ajustado)


    for num, data in enumerate(lista_final):
        if num % 2 == 0:
            print(f'{data:<25}\t',end= '')
        else:
            idade = int(data)
            if idade > 18:
                print(f'{cor["vermelho"]}{idade:>8} anos{cor["limpa"]}\t')
            else:
                print(f'{cor["verde"]}{idade:>8} anos{cor["limpa"]}\t')




























