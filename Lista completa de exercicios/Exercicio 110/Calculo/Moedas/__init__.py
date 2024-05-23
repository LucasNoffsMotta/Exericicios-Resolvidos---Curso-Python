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



def moeda(num=0,moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')


def resumo(num,x=10,y=15):
    print('-'*50)
    print(f'{"RESUMO DO VALOR":^25}')
    print('-'*50)
    print(f'{"Preco analisado:"} \t{moeda(num)}')
    print(f'Dobro do preco: \t{dobro(num,True)}')
    print(f'Metade do preco: \t{metade(num,True)}')
    print(f'{x}% de aumento: \t{aumento(num,x,True)} ')
    print(f'{y}% de aumento: \t{aumento(num,y,True)}')
    print('-' * 50)

