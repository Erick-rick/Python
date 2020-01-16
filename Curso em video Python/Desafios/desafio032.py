ano = int(input('Digite um ano?'))

if (ano %4 ==0) && (ano % 100):
    print('Ano Bisexto')
else:
    print('Ano não Bissexto')