'''
Os percentis são usados ​​nas estatísticas para fornecer um número que descreve o valor em que uma determinada porcentagem dos valores é menor que
'''


import numpy
'''
Qual é o percentil 75? A resposta é 43, o que significa que 75% das pessoas têm 43 anos ou menos.
O módulo NumPy possui um método para encontrar o percentil especificado:
'''

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)

print('Qual é a idade em que 90% das pessoas são mais jovens?')

ages1 = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

y = numpy.percentile(ages1, 90)

print(y)

