caixa = 1
soma = 0

while (caixa <= 5 ):
    print('Numero de caixa : \n', caixa )
    caixa += 1
    peso = float(input('Digite o peso da caixa :\n'))
    soma += peso
else:
    print('peso total :{} '.format(soma))