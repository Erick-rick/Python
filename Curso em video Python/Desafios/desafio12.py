preco = float(input('Qual é o preço do produto :R$ '))

#10 % == 10*5/100
#10% de 1500 == 1500*10/100
# 15% de 875 == 875*15/100

novo = preco (preco * 5 / 100)

print('O preço do produto é R${}, Com desconto de 5% vai custar R${}'.format(preco, novo))
