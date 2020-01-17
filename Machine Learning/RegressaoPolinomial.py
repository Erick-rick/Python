import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

#O NumPy possui um método que permite criar um modelo polinomial:
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

#Em seguida, especifique como a linha será exibida, começamos na posição 1 e terminamos na posição 22:
myline = numpy.linspace(1, 22, 100)

#Desenhe o gráfico de dispersão original:
plt.scatter(x, y)

#Desenhe a linha de regressão polinomial:
plt.plot(myline, mymodel(myline))

#Exiba o diagrama:
plt.show()


#Exemplo
#Preveja a velocidade de um carro que passa às 17:00:

from sklearn.metrics import r2_score

a = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
b = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(a, b, 3))

speed1 = mymodel(17)
print(speed1)