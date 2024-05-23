

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



def moeda(num):

    mostrar = round(num,2)
    num = str(mostrar)

    numeros = ['0','1','2','3','4','5','6','7','8','9']

    for letra in num:
        if letra not in numeros:
            novo = num.replace('.',',')
            return f'R$ {novo}'





def resumo(num,x,y):
    print('-'*50)
    print(f'{"RESUMO DO VALOR":^25}')
    print('-'*50)
    print(f'{"Preco analisado:"} {moeda(num):>19}')
    print(f'Dobro do preco: {dobro(num,True):>20}')
    print(f'Metade do preco: {metade(num,True):>19}')
    print(f'{x}% de aumento: {aumento(num,x,True):>20} ')
    print(f'{y}% de aumento: {aumento(num,y,True):>20}')
    print('-' * 50)
