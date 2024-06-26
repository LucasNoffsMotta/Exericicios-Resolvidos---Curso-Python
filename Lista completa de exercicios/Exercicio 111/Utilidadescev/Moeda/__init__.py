

def metade(num,formata = False):
    if formata:
        num = num/2
        return moeda(num)
    else:
        return num/2



def dobro(num,formata = False):
    if formata:
        num *= 2
        return moeda(num)
    else:
        return num*2


def aumento(num,percent,formata=False):
    if formata:
        num += (num * (percent/100))
        return moeda(num)
    else:
        return num + (num*(percent/100))



def moeda(num,moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')


def resumo(num,x,y):
    print('-'*50)
    print(f'{"RESUMO DO VALOR":^25}')
    print('-'*50)
    print(f'{"Preco analisado:"} {num:>19}')
    print(f'Dobro do preco: {dobro(num,True):>20}')
    print(f'Metade do preco: {metade(num,True):>19}')
    print(f'{x}% de aumento: {aumento(num,x,True):>20} ')
    print(f'{y}% de aumento: {aumento(num,y,True):>20}')
    print('-' * 50)

def cores():
    cores = {
        'limpa': '\033[m',
        'azul': '\033[34m',
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'roxo': '\033[35m',
        'ciano': '\033[36m',
        'branco': '\033[37m',
        'preto': '\033[30m',
        'fundo_azul': '\033[44m',
        'fundo_vermelho': '\033[41m',
        'fundo_verde': '\033[42m',
        'fundo_amarelo': '\033[43m',
        'fundo_roxo': '\033[45m',
        'fundo_ciano': '\033[46m',
        'fundo_branco': '\033[47m',
        'negrito': '\033[1m',
        'reverso': '\033[7m',
        'fundo_preto': '\033[40m',
        'fundo_negrito': '\033[1;7m',
        'fundo_limpa': '\033[0m',
        'sublinhado': '\033[4m',
        'fundo_sublinhado': '\033[4;7m',
        'brilhante': '\033[1m',
        'fraco': '\033[2m',
        'invertido': '\033[3m',
        'oculto': '\033[8m',
        'fundo_preto_brilhante': '\033[100m',
        'fundo_vermelho_brilhante': '\033[101m',
        'fundo_verde_brilhante': '\033[102m',
        'fundo_amarelo_brilhante': '\033[103m',
        'fundo_azul_brilhante': '\033[104m',
        'fundo_roxo_brilhante': '\033[105m',
        'fundo_ciano_brilhante': '\033[106m',
        'fundo_branco_brilhante': '\033[107m',
        'fundo_preto_fraco': '\033[90m',
        'fundo_vermelho_fraco': '\033[91m',
        'fundo_verde_fraco': '\033[92m',
        'fundo_amarelo_fraco': '\033[93m',
        'fundo_azul_fraco': '\033[94m',
        'fundo_roxo_fraco': '\033[95m',
        'fundo_ciano_fraco': '\033[96m',
        'fundo_branco_fraco': '\033[97m',
        'fundo_reset': '\033[49m',
        'brilho_limpa': '\033[21m',
        'fraco_limpa': '\033[22m',
        'normal_limpa': '\033[23m',
        'invertido_limpa': '\033[27m',
        'oculto_limpa': '\033[28m'
    }

    return cores


