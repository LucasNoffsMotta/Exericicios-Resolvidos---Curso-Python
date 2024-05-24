import cores

cor = cores.cores()


def mostra_titulo(txt):
    tam = (len(txt)) + 15

    print('-'*tam)
    print(txt.center(tam))
    print('-'*tam)

def valida_num(txt):

    while True:
        print('-'*29)
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

    with open('pessoas.txt','a') as file:
        for pessoa in pessoas_cadastradas:
            file.write(pessoa + '\n')

    file.close()



def le_pessoas():

    nova_lista = []
    pessoa = dict()
    with open('pessoas.txt','r') as documento:

        linha = documento.readlines()
        for items in linha:
            if items.isnumeric():
                pessoa['idade'] = items
            else:
                pessoa['nome'] = items
        nova_lista.append(pessoa)


    documento.close()

    return nova_lista


def le_lista(nova_lista):


    print(nova_lista)



    #for cont,items in enumerate(nova_lista):
     #   if cont % 2 == 0:
      #      print(f'{nova_lista[cont]}',end = '   ')
       # else:
        #    print(f'{nova_lista[cont]}',end = '')

















