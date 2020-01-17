#Para visualizar o conjunto de dados, podemos desenhar um histograma com os dados que coletamos.
#

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()


'''Crie uma matriz com 100000 números aleatórios e exiba-os usando um histograma com 100 barras:
'''
y = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(y, 100)
plt.show()