print ('--Valor do produto com desconto -- ')

pr = float(input('Digite o valor do produto : '))

d = float(input('Digite o valor do desconto do produto :'))

pag = (pr * d /100)

novo = pr -(pr * d /100)


print('O preço do produto é {}\ncom {}% de desconto {}\ntotal : {}'.format(pr, d, pag,novo))


