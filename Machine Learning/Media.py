#Modo == Mediano=== medio
# Velocidade de 13 carros:

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

import numpy

x = numpy.mean(speed)

# Mediana

y = numpy.median(speed)

# Modo
from scipy import stats

z = stats.modo(speed)

print('Media :' + x)
print('Mediana : '+ y)
print('Modo :' + z)