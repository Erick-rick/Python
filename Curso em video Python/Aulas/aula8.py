
# import math >> importa tudo
# ceil > arredondamento para cima
# floor >arredondamento para baixo
# trunc > trunca o numero, eliminando da virgula para frente
# pow > potencia
# sqrt > raiz quadrada
# factorial > fatorial

from math import sqrt, ceil

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz)) #.2f > duas casa decimas depois da virgula
print('----------------------------------------------------------------------------------------------')

import random

number = random.random()
number1 = random.randint(1, 10)
print (number)
print('---------------------')
print(number1)

print('-----------------------------------------------')

import emoji
print(emoji.emojiza('Olá mundo: earth_americas:', use_aliases= True))
