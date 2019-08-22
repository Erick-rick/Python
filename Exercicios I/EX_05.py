print ('--Valor do produto com desconto -- ')

pr = float(input('Digite o valor do produto : '))

desc = float(input('Digite o valor do desconto do produto :'))

pag = (pr * desc /100)

precof = pr -(pr * desc /100)


print('O preço do produto é {}\ncom {}% de desconto {}\ntotal : {}'.format(pr, desc, pag, precof))
