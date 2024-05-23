

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

cor = cores()

def leiaDinheiro(txt):

    while True:

        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        num = str(input(txt))
        novo =str
        if num.isnumeric():
            num = int(num)
            return num

        else:
            for letra in num:
                if letra not in numeros:
                    novo = num.replace(letra,'.')

        try:
            float(novo)
            if float(novo):
                novo = float(novo)
                return novo

        except ValueError:
            print(f'{cor["vermelho"]}ERROR! {num} is not numeric.{cor["limpa"]}')

















