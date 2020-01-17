# DESVIO PADRÃO
#Use o std()método NumPy para encontrar o desvio padrão
'''Um desvio padrão baixo significa que a maioria dos números está próxima do valor médio (médio).
Um desvio padrão alto significa que os valores estão distribuídos em uma faixa mais ampla.

Isso significa que a maioria dos valores está dentro da faixa de 37,85 a partir do valor médio, que é 77,4.
Como você pode ver, um desvio padrão mais alto indica que os valores estão distribuídos em uma faixa mais ampla.'''

import numpy

speed = [86,87,88,86,87,85,86]
speed1 = [32,111,138,28,59,77,97]

x = numpy.std(speed)
y = numpy.std(speed1)

print(x, y)

# VARIAÇÃO
'''Variação é outro número que indica como os valores estão espalhados.
De fato, se você pegar a raiz quadrada da variação, obterá a variação padrão!
Ou o contrário, se você multiplicar o desvio padrão por si só, obtém a variação!

'''

import numpy

speed = [32,111,138,28,59,77,97]

z = numpy.var(speed)

print(z)