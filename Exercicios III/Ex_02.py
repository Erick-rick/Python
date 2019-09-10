
quantidade = 1 
total = 0
 
while (quantidade <= 45):
    print('Produto nº ', quantidade)
    quantidade +=1
    preco = float(input('Digite o preco do produto :\n'))
    total += preco
else:
    print ('Valor total : \n >>>>{}'.format(total))
