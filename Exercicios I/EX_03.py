print ('--Valor monétario do desconto -- ')

preco = float(input('Digite o valor do produto : '))

d = (preco * 5 /100)

novo = preco -(preco * 5 /100)

print('O preço do produto é {}\ncom 5% de desconto {}\ntotal : {}'.format(preco, d, novo))