from Cores import cores

cor = cores()

def leiaDinheiro(txt):

    while True:

        num = str(input(txt))

        if num.isnumeric():
            num = float(num)
            return num

        else:
            print(f'{cor["vermelho"]}ERROR! {num} is not numeric.')







