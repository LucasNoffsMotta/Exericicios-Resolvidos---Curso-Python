from Colors import cores

cor = cores()

def leiaInt(txt):

    while True:

        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print(f'{cor["vermelho"]}Digite um valor inteiro valido.{cor["limpa"]}')
            continue
        except KeyboardInterrupt:
            print(f'{cor["vermelho"]}Entrada de dados interrompida pelo usuario.')
            n = 0
            return n
        else:
            return n

def leiaFloat(txt):

    while True:
        try:
           n = float(input(txt))
        except (ValueError,TypeError):
            print(f'{cor["vermelho"]}Digite um valor real valido.{cor["limpa"]}')
        except KeyboardInterrupt:
            print(f'{cor["vermelho"]}Entrada de dados interrompida pelo usuario.{cor["limpa"]}')
            n=0
            return n
        else:
            return n






n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero real valido: ')
print(f'O valor inteiro digitado = {n1}')
print(f'O valor real digitado = {n2}')

