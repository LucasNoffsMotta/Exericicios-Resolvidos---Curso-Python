
def check_file():
    try:
        a = open('Dados.text','rt')
        a.close()
    except FileNotFoundError:
        return False

    else:
        return True



def make_file(nome):

    try:
        a = open(nome,'a+')
        a.close()
    except:
        print('Houve um ERRO na criacao do arquivo.')




def read_file(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<10}{dado[1]:>4} anos\t')

    finally:
        a.close()

def cadastrar(arq,nome='desconhecido',idade=0):

    try:
        a = open(arq,'a')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao salvar dados no arquivo.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()



























