import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

#Comece com um conjunto de dados que você deseja testar.
#Nosso conjunto de dados ilustra 100 clientes em uma loja e seus hábitos de compra.

#
# O eixo x representa o número de minutos antes de fazer uma compra.
O eixo y representa a quantia gasta na compra.
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x



# O conjunto de treinamento deve ser uma seleção aleatória de 80% dos dados originais.
#O conjunto de testes deve ser os 20% restantes.
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()